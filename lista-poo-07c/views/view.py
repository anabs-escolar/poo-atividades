from dao import ClienteDAO, CategoriaDAO, ProdutoDAO
from models import Cliente, Categoria, Produto


class View:
    def abrir_todos() -> None:
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()

    def cliente_autenticar(email: str, senha: str) -> dict | None:
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
