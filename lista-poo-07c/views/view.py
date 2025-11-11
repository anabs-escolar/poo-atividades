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

    def cliente_autenticar(email: str, senha: str) -> object | None:
        for obj in ClienteDAO.listar():
            if (obj.get_email() == email) and (obj.get_senha() == senha):
                return obj
        return None

    def cliente_listar() -> list[Cliente]:
        return ClienteDAO.listar()

    def cliente_inserir(nome: str, email: str, senha: str, fone: str) -> None:
        cliente = Cliente(0, nome, email, senha, fone)
        ClienteDAO.inserir(cliente)

    def cliente_atuazlizar(
        id: int, nome: str, email: str, senha: str, fone: str
    ) -> None:
        cliente = Cliente(id, nome, email, senha, fone)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id: int) -> None:
        for i in ClienteDAO.listar():
            if i.get_id() == id:
                ClienteDAO.excluir(i)
                break

    def categoria_listar() -> list[Categoria]:
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str) -> None:
        categoria = Categoria(0, descricao)
        CategoriaDAO.inserir(categoria)

    def categoria_atualizar(id: int, descricao: str) -> None:
        categoria = Categoria(id, descricao)
        CategoriaDAO.atualizar(categoria)

    def categoria_excluir(id: int) -> None:
        for i in CategoriaDAO.listar():
            if i.get_id == id:
                CategoriaDAO.excluir(i)
                break

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
        produto = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(produto)

    def produto_excluir(id: int) -> None:
        for i in Produto.listar():
            if i.get_id == id:
                ProdutoDAO.excluir(i)
                break

    def produto_reajustar(percentual: float) -> None:
        pass

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
