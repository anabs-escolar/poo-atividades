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
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        if not email.strip():
            raise ValueError("Email não pode ser vazio.")
        if not senha.strip():
            raise ValueError("Senha não pode ser vazia.")
        if not fone.strip():
            raise ValueError("Telefone não pode ser vazio.")

        for c in ClienteDAO.listar():
            if c.get_email() == email:
                raise ValueError("Já existe um cliente com esse e-mail.")

        cliente = Cliente(0, nome, email, senha, fone, is_admin)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id: int, nome: str, email: str, fone: str) -> None:
        cliente = ClienteDAO.listar_id(id)
        if not cliente:
            raise ValueError("Cliente não encontrado.")

        if nome is not None and not nome.strip():
            raise ValueError("Nome não pode ser vazio.")

        if email is not None and not email.strip():
            raise ValueError("Email não pode ser vazio.")

        if fone is not None and not fone.strip():
            raise ValueError("Telefone não pode ser vazio.")

        if email.strip():
            for c in ClienteDAO.listar():
                if c.get_id() != id and c.get_email() == email:
                    raise ValueError("Já existe um cliente com esse e-mail.")
            cliente.set_email(email)

        if nome.strip():
            cliente.set_nome(nome)

        if fone.strip():
            cliente.set_fone(fone)

        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        if not c:
            raise ValueError("Cliente não encontrado.")

        for v in VendaDAO.listar():
            if v.get_id_cliente() == id:
                raise ValueError(
                    "Cliente associado a uma Venda - não pode ser excluído."
                )

        ClienteDAO.excluir(c)

    def adicionar_admin(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        if not c:
            raise ValueError("Cliente não encontrado.")

        if c.get_is_admin():
            raise ValueError("O cliente já é administrador.")

        c.set_is_admin(True)
        ClienteDAO.atualizar(c)

    def remover_admin(id: int) -> None:
        c = ClienteDAO.listar_id(id)
        if not c:
            raise ValueError("Cliente não encontrado.")

        if not c.get_is_admin():
            raise ValueError("O cliente não é administrador.")

        c.set_is_admin(False)
        ClienteDAO.atualizar(c)

    def categoria_listar() -> list[Categoria]:
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str) -> None:
        if not descricao.strip():
            raise ValueError("Descrição da categoria não pode ser vazia.")

        for c in CategoriaDAO.listar():
            if c.get_descricao() == descricao:
                raise ValueError("Essa descrição de Categoria já está cadastrada.")
        categoria = Categoria(0, descricao)
        CategoriaDAO.inserir(categoria)

    def categoria_atualizar(id: int, descricao: str) -> None:
        categoria = CategoriaDAO.listar_id(id)
        if not categoria:
            raise ValueError("Categoria não encontrada")
        if not descricao.strip():
            raise ValueError("Descrição da categoria não pode ser vazia.")
        if descricao.strip():
            for c in CategoriaDAO.listar():
                if c.get_descricao() == descricao:
                    raise ValueError("Essa descrição de Categoria já está cadastrada.")
            categoria.set_descricao(descricao)
        CategoriaDAO.atualizar(categoria)

    def categoria_excluir(id: int) -> None:
        c = CategoriaDAO.listar_id(id)
        if not c:
            raise ValueError("Categoria não encontrada.")

        for p in ProdutoDAO.listar():
            if p.get_id_categoria() == id:
                raise ValueError(
                    "Categoria usada em Produtos — exclusão não permitida."
                )

        CategoriaDAO.excluir(c)

    def produto_listar() -> list[Produto]:
        return ProdutoDAO.listar()

    def produto_inserir(
        descricao: str, preco: float, estoque: int, id_categoria: int
    ) -> None:
        if not descricao.strip():
            raise ValueError("Descrição do produto não pode ser vazia.")

        if preco is None or preco == "":
            raise ValueError("Preço não pode ser vazio.")

        if estoque is None or estoque == "":
            raise ValueError("Estoque não pode ser vazio.")

        if id_categoria is None:
            raise ValueError("A categoria não pode ser vazia.")

        c = CategoriaDAO.listar_id(id_categoria)
        if c is None:
            raise ValueError("Categoria não encontrada.")

        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")

        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")

        produtos = ProdutoDAO.listar()
        for p in produtos:
            if p.get_descricao() == descricao:
                raise ValueError("Produto já existe.")

        produto = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(produto)

    def produto_atualizar(
        id: int, descricao: str, preco: float, estoque: int, id_categoria: int
    ) -> None:
        produto = ProdutoDAO.listar_id(id)
        if not produto:
            raise ValueError("Produto não encontrado.")

        if not descricao.strip():
            raise ValueError("Descrição do produto não pode ser vazia.")

        if preco is None or preco == "":
            raise ValueError("Preço não pode ser vazio.")

        if estoque is None or estoque == "":
            raise ValueError("Estoque não pode ser vazio.")

        if id_categoria is None:
            raise ValueError("A categoria não pode ser vazia.")

        categoria = CategoriaDAO.listar_id(id_categoria)
        if not categoria:
            raise ValueError("Categoria não encontrada.")

        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero.")
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")

        for p in ProdutoDAO.listar():
            if p.get_id() != id and p.get_descricao() == descricao:
                raise ValueError("Já existe outro produto com essa descrição.")

        if descricao.strip():
            produto.set_descricao(descricao)
        produto.set_preco(preco)
        produto.set_estoque(estoque)
        produto.set_id_categoria(id_categoria)

        ProdutoDAO.atualizar(produto)

    def produto_excluir(id: int) -> None:
        for vi in VendaItemDAO.listar():
            if vi.get_id_produto() == id:
                raise ValueError(
                    "Produto não pode ser excluído porque está associada a uma Venda."
                )

        p = ProdutoDAO.listar_id(id)
        ProdutoDAO.excluir(p)

    def produto_reajustar(percentual: float) -> None:
        if percentual == "" or percentual is None:
            raise ValueError("Percentual não pode ser vazio.")

        for p in ProdutoDAO.listar():
            p.set_preco(p.get_preco() * (percentual + 1))
            ProdutoDAO.atualizar(p)

    def produto_inserir_carrinho(id_produto: int, id_cliente: int, qtd: int) -> None:
        if qtd is None or qtd == "":
            raise ValueError("Quantidade não pode ser vazia.")

        if qtd <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")

        produto = ProdutoDAO.listar_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado.")
        if qtd <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        if qtd > produto.get_estoque():
            raise ValueError("Quantidade maior que o estoque disponível.")

        venda = None
        for v in VendaDAO.listar():
            if v.get_id_cliente() == id_cliente and v.get_carrinho():
                venda = v
                break

        if not venda:
            venda = Venda(0, datetime.now(), True, 0.0, id_cliente)
            VendaDAO.inserir(venda)

        item = None
        for vi in VendaItemDAO.listar():
            if (
                vi.get_id_venda() == venda.get_id()
                and vi.get_id_produto() == id_produto
            ):
                item = vi
                break

        if item:
            nova_qtd = item.get_qtd() + qtd
            item.set_qtd(nova_qtd)
            item.set_preco(nova_qtd * produto.get_preco())
            VendaItemDAO.atualizar(item)
        else:
            novo_item = VendaItem(
                0, venda.get_id(), id_produto, qtd, qtd * produto.get_preco()
            )
            VendaItemDAO.inserir(novo_item)

        total = sum(
            vi.get_preco()
            for vi in VendaItemDAO.listar()
            if vi.get_id_venda() == venda.get_id()
        )
        venda.set_total(total)
        VendaDAO.atualizar(venda)

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
        itens, total = View.carrinho_listar(id_cliente)
        if not itens:
            raise ValueError("Carrinho vazio.")

        venda = None
        for v in VendaDAO.listar():
            if v.get_id_cliente() == id_cliente and v.get_carrinho():
                venda = v
                break

        if not venda:
            raise ValueError("Nenhuma venda aberta encontrada.")

        for vi in VendaItemDAO.listar():
            if vi.get_id_venda() == venda.get_id():
                produto = ProdutoDAO.listar_id(vi.get_id_produto())
                if produto:
                    novo_estoque = produto.get_estoque() - vi.get_qtd()
                    produto.set_estoque(max(0, novo_estoque))
                    ProdutoDAO.atualizar(produto)

        venda.set_carrinho(False)
        VendaDAO.atualizar(venda)

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
                            "id_produto": prod.get_id(),
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
