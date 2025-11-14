from datetime import datetime

from data import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO
from models import Cliente, Categoria, Produto, Venda, VendaItem


class View:
    def abrir_todos() -> None:
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()
        VendaDAO.abrir()
        VendaItemDAO.abrir()

    def cliente_autenticar(email: str, senha: str) -> Cliente | None:
        for obj in ClienteDAO.listar():
            if (obj.get_email() == email) and (obj.get_senha() == senha):
                return obj
        return None

    def cliente_listar() -> list[Cliente]:
        return ClienteDAO.listar()

    def cliente_inserir(
        nome: str, email: str, senha: str, fone: str, is_admin: bool = False
    ) -> None:
        cliente = Cliente(0, nome, email, senha, fone, is_admin)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id: int, nome: str, email: str, fone: str) -> None:
        cliente = ClienteDAO.listar_id(id)
        if not cliente:
            print("Cliente não encontrado.")
            return
        if nome.strip():
            cliente.set_nome(nome)
        if email.strip():
            cliente.set_email(email)
        if fone.strip():
            cliente.set_fone(fone)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        ClienteDAO.excluir(c)

    def adicionar_admin(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        if not c:
            print("Cliente não encontrado.")
            return
        c.set_is_admin(True)
        ClienteDAO.atualizar(c)

    def remover_admin(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        if not c:
            print("Cliente não encontrado.")
            return
        c.set_is_admin(False)
        ClienteDAO.atualizar(c)

    def categoria_listar() -> list[Categoria]:
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str) -> None:
        categoria = Categoria(0, descricao)
        CategoriaDAO.inserir(categoria)

    def categoria_atualizar(id: int, descricao: str) -> None:
        categoria = CategoriaDAO.listar_id(id)
        if not categoria:
            print("Categoria não encontrada")
            return
        if descricao.strip():
            categoria.set_descricao(descricao)
        CategoriaDAO.atualizar(categoria)

    def categoria_excluir(id: int) -> None:
        c = CategoriaDAO.listar_id(id)
        CategoriaDAO.excluir(c)

    def produto_listar() -> list[Produto]:
        return ProdutoDAO.listar()

    def produto_inserir(
        descricao: str, preco: float, estoque: int, id_categoria: int
    ) -> None:
        produto = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(produto)

    def produto_atualizar(
        id: int, descricao: str, preco: float, estoque: int, id_categoria: int
    ) -> None:
        produto = ProdutoDAO.listar_id(id)
        if not produto:
            print("Produto não encontrado.")
        if descricao.strip():
            produto.set_descricao(descricao)
        if preco:
            produto.set_preco(preco)
        if estoque:
            produto.set_estoque(estoque)
        if id_categoria:
            produto.set_id_categoria(id_categoria)
        ProdutoDAO.atualizar(produto)

    def produto_excluir(id: int) -> None:
        p = ProdutoDAO.listar_id(id)
        ProdutoDAO.excluir(p)

    def produto_reajustar(percentual: float) -> None:
        for p in ProdutoDAO.listar():
            p.set_preco(p.get_preco() * (percentual + 1))

    def produto_inserir_carrinho(id_produto: int, id_cliente: int, qtd: int) -> None:
        venda_aberta = None
        for venda in VendaDAO.listar():
            if venda.get_id_cliente() == id_cliente and venda.get_carrinho():
                venda_aberta = venda
                break

        if venda_aberta is None:
            venda_aberta = Venda(0, datetime.now(), True, 0.0, id_cliente)
            VendaDAO.inserir(venda_aberta)

        produto = ProdutoDAO.listar_id(id_produto)

        item = None
        for vi in VendaItemDAO.listar():
            if (
                vi.get_id_venda() == venda_aberta.get_id()
                and vi.get_id_produto() == id_produto
            ):
                item = vi

        if item:
            novo_qtd = item.get_qtd() + qtd
            novo_preco = novo_qtd * produto.get_preco()

            item.set_qtd(novo_qtd)
            item.set_preco(novo_preco)

            VendaItemDAO.atualizar(item)
        else:
            item = VendaItem(
                0, venda_aberta.get_id(), id_produto, qtd, qtd * produto.get_preco()
            )
            VendaItemDAO.inserir(item)

        total = 0.0
        for vi in VendaItemDAO.listar():
            if venda_aberta.get_id() == vi.get_id_venda():
                total += vi.get_preco()
        venda_aberta.set_total(total)
        VendaDAO.atualizar(venda_aberta)

    def carrinho_listar(id_cliente: int) -> tuple[list[dict], float]:
        venda_aberta = None
        for v in VendaDAO.listar():
            if v.get_id_cliente() == id_cliente and v.get_carrinho():
                venda_aberta = v
                break

        if venda_aberta is None:
            return [], 0.0

        itens: list[dict] = []
        for vi in VendaItemDAO.listar():
            if vi.get_id_venda() == venda_aberta.get_id():
                produto = ProdutoDAO.listar_id(vi.get_id_produto())
                preco_unit = vi.get_preco() / vi.get_qtd() if vi.get_qtd() else 0.0
                descricao = ""

                if produto:
                    descricao = produto.get_descricao()
                    preco_unit = produto.get_preco()

                itens.append(
                    {
                        "id_produto": vi.get_id_produto(),
                        "descricao": descricao,
                        "preco_unitario": preco_unit,
                        "qtd": vi.get_qtd(),
                        "total_item": vi.get_preco(),
                    }
                )

        return itens, venda_aberta.get_total()

    def carrinho_comprar(id_cliente: int) -> None:
        venda_aberta = None
        for v in VendaDAO.listar():
            if v.get_id_cliente() == id_cliente and v.get_carrinho():
                venda_aberta = v
                for vi in VendaItemDAO.listar():
                    if vi.get_id_venda() == venda_aberta.get_id():
                        produto = ProdutoDAO.listar_id(vi.get_id_produto())
                        if produto:
                            novo_estoque = produto.get_estoque() - vi.get_qtd()
                            if novo_estoque < 0:
                                novo_estoque = 0
                            produto.set_estoque(novo_estoque)
                            ProdutoDAO.atualizar(produto)
        venda_aberta.set_carrinho(False)
        VendaDAO.atualizar(venda_aberta)

    def compras_listar(id_cliente: int) -> list[tuple[Venda, list[dict]]]:
        compras = []
        items = []
        for v in VendaDAO.listar():
            if v.get_id_cliente() == id_cliente and not v.get_carrinho():
                for vi in VendaItemDAO.listar():
                    if vi.get_id_venda() == v.get_id():
                        prod = ProdutoDAO.listar_id(vi.get_id_produto())
                        item = {
                            "descricao": prod.get_descricao(),
                            "preco_uni": prod.get_preco(),
                            "preco_qtd": vi.get_preco(),
                            "qtd": vi.get_qtd(),
                        }
                        items.append(item)
                compras.append((v, items))
            items = []
        return compras

    def vendas_listar() -> list[tuple[dict, list[dict]]]:
        vendas = []
        items = []
        for v in VendaDAO.listar():
            if not v.get_carrinho():
                for vi in VendaItemDAO.listar():
                    if vi.get_id_venda() == v.get_id():
                        prod = ProdutoDAO.listar_id(vi.get_id_produto())
                        item = {
                            "descricao": prod.get_descricao(),
                            "preco_uni": prod.get_preco(),
                            "preco_qtd": vi.get_preco(),
                            "qtd": vi.get_qtd(),
                        }
                        items.append(item)
                cliente = ClienteDAO.listar_id(v.get_id_cliente())
                venda = {
                    "cliente": cliente.get_nome() if cliente else "Cliente Excluido",
                    "total": v.get_total(),
                    "data": v.get_data(),
                }
                vendas.append((venda, items))
            items = []
        return vendas
