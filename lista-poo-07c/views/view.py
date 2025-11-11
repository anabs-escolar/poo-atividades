from datetime import datetime

from data import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO
from models import Cliente, Categoria, Produto, Venda, VendaItem


class View:
    def abrir_todos() -> None:
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()

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
            venda_aberta = Venda(0, id_cliente, True, datetime.now())
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
            antigo_preco = item.get_preco()
            novo_qtd = item.get_qtd() + qtd
            novo_preco = novo_qtd * produto.get_preco()

            item.set_qtd(novo_qtd)
            item.set_preco(novo_preco)

            VendaItemDAO.atualizar(item)
            venda_aberta.set_total(
                venda_aberta.get_total() + (novo_preco - antigo_preco)
            )
        else:
            item = VendaItem(
                0, venda_aberta.get_id(), id_produto, qtd, qtd * produto.get_preco()
            )
            VendaItemDAO.inserir(item)
            venda_aberta.set_total(qtd * produto.get_preco())

        VendaDAO.atualizar(venda_aberta)
