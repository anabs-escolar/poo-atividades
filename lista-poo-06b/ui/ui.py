import os
from dao import CategoriaDAO, ProdutoDAO, ClienteDAO, VendaDAO, VendaItemDAO
from models import Categoria, Produto, Cliente


class UI:
    @staticmethod
    def clean() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def main() -> None:
        CategoriaDAO.abrir()
        ClienteDAO.abrir()
        ProdutoDAO.abrir()
        while True:
            UI.clean()
            op = UI.menu()
            if op == 1:
                UI.produto_menu()
            elif op == 2:
                UI.categoria_menu()
            elif op == 3:
                UI.cliente_menu()
            elif op == 0:
                break

    @staticmethod
    def menu() -> int:
        print("=== Menu Principal ===")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Categorias")
        print("3. Gerenciar Clientes")
        print("0. Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def produto_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Produtos ===")
            print("1. Inserir Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Excluir Produto")
            print("0. Voltar")
            op = int(input("Escolha uma opção: "))
            if op == 1:
                UI.produto_inserir()
            elif op == 2:
                UI.produto_listar()
            elif op == 3:
                UI.produto_atualizar()
            elif op == 4:
                UI.produto_excluir()
            elif op == 0:
                break

    @staticmethod
    def categoria_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Categoria ===")
            print("1. Inserir Categoria")
            print("2. Listar Categorias")
            print("3. Atualizar Categoria")
            print("4. Excluir Categoria")
            print("0. Voltar")
            op = int(input("Escolha uma opção: "))
            if op == 1:
                UI.categoria_inserir()
            elif op == 2:
                UI.categoria_listar()
            elif op == 3:
                UI.categoria_atualizar()
            elif op == 4:
                UI.categoria_excluir()
            elif op == 0:
                break

    @staticmethod
    def cliente_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Clientes ===")
            print("1. Inserir Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("0. Voltar")
            op = int(input("Escolha uma opção: "))
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_listar()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_excluir()
            elif op == 0:
                break

    @staticmethod
    def produto_inserir() -> None:
        UI.clean()
        print("=== Inserir Produto ===")

        id = int(input("ID: "))
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))

        print("Categorias disponíveis:")
        categorias = CategoriaDAO.listar()
        for categoria in categorias:
            print("\t", categoria)
        id_categoria = int(input("ID da Categoria: "))

        produto = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(produto)
        print(f"Produto {produto.get_descricao()} inserido com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def produto_listar() -> None:
        UI.clean()
        print("=== Lista de Produtos ===")

        produtos = ProdutoDAO.listar()
        if not produtos:
            print("Nenhum produto cadastrado!")
            return
        for produto in produtos:
            print(produto)
        input("Pressione Enter para continuar...")

    @staticmethod
    def produto_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Produto ===")

        id = int(input("ID do produto a atualizar: "))
        produto = ProdutoDAO.listar_id(id)
        if produto is None:
            print("Produto não encontrado!")
            return
        produto.set_descricao(input("Nova descrição: "))
        produto.set_preco(float(input("Novo preço: ")))
        produto.set_estoque(int(input("Novo estoque: ")))
        ProdutoDAO.atualizar(produto)
        print(f"Produto {produto.get_descricao()} atualizado com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def produto_excluir() -> None:
        UI.clean()
        print("=== Excluir de Produtos ===")

        id = int(input("ID do produto a excluir: "))
        produto = ProdutoDAO.listar_id(id)
        if produto is None:
            print("Produto não encontrado!")
            return
        ProdutoDAO.excluir(produto)
        print(f"Produto {produto.get_descricao()} excluído com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def categoria_inserir() -> None:
        UI.clean()
        print("=== Inserir Categoria ===")

        id = int(input("ID: "))
        descricao = input("Descrição: ")
        categoria = Categoria(id, descricao)
        CategoriaDAO.inserir(categoria)
        print(f"Categoria {categoria.get_descricao()} inserida com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def categoria_listar() -> None:
        UI.clean()
        print("=== Lista de Categorias ===")

        categorias = CategoriaDAO.listar()
        if not categorias:
            print("Nenhuma categoria cadastrada!")
            return
        for categoria in categorias:
            print(categoria)
        input("Pressione Enter para continuar...")

    @staticmethod
    def categoria_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Categoria ===")

        id = int(input("ID da categoria a atualizar: "))
        categoria = CategoriaDAO.listar_id(id)
        if categoria is None:
            print("Categoria não encontrada!")
            return
        categoria.set_descricao(input("Nova descrição: "))
        CategoriaDAO.atualizar(categoria)
        print(f"Categoria {categoria.get_descricao()} atualizada com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def categoria_excluir() -> None:
        UI.clean()
        print("=== Excluir Categoria ===")

        id = int(input("ID da categoria a excluir: "))
        categoria = CategoriaDAO.listar_id(id)
        if categoria is None:
            print("Categoria não encontrada!")
            return
        CategoriaDAO.excluir(categoria)
        print(f"Categoria {categoria.get_descricao()} excluída com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def cliente_listar() -> None:
        UI.clean()
        print("=== Lista de Clientes ===")

        clientes = ClienteDAO.listar()
        if not clientes:
            print("Nenhum cliente cadastrado!")
            return
        for cliente in clientes:
            print(cliente)
        input("Pressione Enter para continuar...")

    @staticmethod
    def cliente_inserir() -> None:
        UI.clean()
        print("=== Inserir Cliente ===")

        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.inserir(cliente)
        print(f"Cliente {cliente.get_nome()} inserido com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def cliente_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Cliente ===")

        id = int(input("ID do cliente a atualizar: "))
        cliente = ClienteDAO.listar_id(id)
        if cliente is None:
            print("Cliente não encontrado!")
            return
        cliente.set_nome(input("Novo nome: "))
        cliente.set_email(input("Novo email: "))
        cliente.set_fone(input("Novo fone: "))
        ClienteDAO.atualizar(cliente)
        print(f"Cliente {cliente.get_nome()} atualizado com sucesso!")
        input("Pressione Enter para continuar...")

    @staticmethod
    def cliente_excluir() -> None:
        UI.clean()
        print("=== Excluir Cliente ===")

        id = int(input("ID do cliente a excluir: "))
        cliente = ClienteDAO.listar_id(id)
        if cliente is None:
            print("Cliente não encontrado!")
            return
        ClienteDAO.excluir(cliente)
        print(f"Cliente {cliente.get_nome()} excluído com sucesso!")
        input("Pressione Enter para continuar...")
