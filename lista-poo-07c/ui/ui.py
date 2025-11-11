import os
from views import View


class UI:
    __usuario = None

    def clean():
        os.system("cls" if os.name == "nt" else "clear")

    def continuar():
        input("\nPrecione ENTER para continuar...")

    def op() -> int:
        return int(input("\nEscolha uma opção: "))

    def main():
        View.abrir_todos()
        UI.menu_visitante()

    def menu_visitante():
        while True:
            UI.clean()
            print("=== Menu de Visitante ===")
            print(
                "1. Entrar no Sistema",
                "2. Abrir Conta",
                "0. Sair",
                sep="\n",
            )
            op = UI.op()
            if op == 1:
                UI.visitante_entrar()
            if op == 2:
                UI.visitante_criar_conta()
            if op == 0:
                break

    @classmethod
    def visitante_entrar(cls):
        UI.clean()
        print("=== Entrar no Sistema ===")
        email = input("Email: ")
        senha = input("Senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario:
            if cls.__usuario.get_is_admin():
                print(f"\nBem-vindo(a), Admin. {cls.__usuario.get_nome()}!")
                UI.continuar()
                UI.menu_admin()
            else:
                print(f"\nBem-vindo(a), {cls.__usuario.get_nome()}!")
                UI.continuar()
                UI.menu_cliente()
        else:
            print("\nAutenticação falhou, confira seus dados.")
            UI.continuar()

    def visitante_criar_conta():
        UI.clean()
        print("=== Criar Conta ===")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        fone = input("Telefone: ")
        View.cliente_inserir(nome, email, senha, fone)
        print("\nConta criada com successo!")
        UI.continuar()
        UI.menu_visitante()

    def menu_admin():
        while True:
            UI.clean()
            print("=== Menu de Administrador ===")
            print(
                "1. Gerenciar Clientes",
                "2. Gerenciar Categorias",
                "3. Gerenciar Produtos",
                "0. Sair",
                sep="\n",
            )
            options = {
                1: UI.cliente_menu,
                2: UI.categoria_menu,
                3: UI.produto_menu,
            }
            op = UI.op()
            if op in options:
                options[op]()
            elif op == 0:
                break

    def menu_cliente():
        while True:
            UI.clean()
            print("=== Menu de Cliente ===")
            print(
                "1. Listar Produtos",
                "2. Inserir Produto no Carrinho",
                "3. Visualizar Carrinho",
                "4. Comprar Carrinho",
                "5. Listar minhas Compras",
                "0. Sair",
                sep="\n",
            )
            options = {
                1: UI.produto_listar,
                2: UI.produto_inserir_carrinho,
                3: UI.carrinho_listar,
                4: UI.carrinho_comprar,
                5: UI.compra_listar,
            }
            op = UI.op()
            if op in options:
                options[op]()
            elif op == 0:
                break

    def produto_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Produtos ===")
            print(
                "1. Inserir Produto",
                "2. Listar Produtos",
                "3. Atualizar Produto",
                "4. Excluir Produto",
                "0. Voltar",
                sep="\n",
            )
            options = {
                1: UI.produto_inserir,
                2: UI.produto_listar,
                3: UI.produto_atualizar,
                4: UI.produto_excluir,
            }
            op = UI.op()
            if op in options:
                options[op]()
            elif op == 0:
                break

    def categoria_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Categoria ===")
            print("1. Inserir Categoria")
            print("2. Listar Categorias")
            print("3. Atualizar Categoria")
            print("4. Excluir Categoria")
            print("0. Voltar")
            op = UI.op()
            options = {
                1: UI.categoria_inserir,
                2: UI.categoria_listar,
                3: UI.categoria_atualizar,
                4: UI.categoria_excluir,
            }
            if op in options:
                options[op]()
            elif op == 0:
                break

    def cliente_menu() -> None:
        while True:
            UI.clean()
            print("=== Menu de Clientes ===")
            print("1. Inserir Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("0. Voltar")
            op = UI.op()
            options = {
                1: UI.cliente_inserir,
                2: UI.cliente_listar,
                3: UI.cliente_atualizar,
                4: UI.cliente_excluir,
            }
            if op in options:
                options[op]()
            elif op == 0:
                break

    def produto_inserir() -> None:
        UI.clean()
        print("=== Inserir Produto ===")

        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))

        print("Categorias disponíveis:")
        categorias = View.categoria_listar()
        for categoria in categorias:
            print("\t", categoria)
        id_categoria = int(input("ID da Categoria: "))

        View.produto_inserir(descricao, preco, estoque, id_categoria)
        print(f"Produto inserido com sucesso!")
        UI.continuar()

    def produto_listar() -> None:
        UI.clean()
        print("=== Lista de Produtos ===")
        produtos = View.produto_listar()
        if not produtos:
            print("Nenhum produto cadastrado!")
            return
        for produto in produtos:
            print(produto)
        UI.continuar()

    def produto_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Produto ===")
        id = int(input("ID do produto a atualizar: "))
        desc = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        est = int(input("Novo estoque: "))
        View.produto_atualizar(id, desc, preco, est)
        print("Produto atualizado com sucesso!")
        UI.continuar()

    def produto_excluir() -> None:
        UI.clean()
        print("=== Excluir de Produtos ===")
        id = int(input("ID do produto a excluir: "))
        View.produto_excluir(id)
        print(f"Produto excluído com sucesso!")
        UI.continuar()

    @classmethod
    def produto_inserir_carrinho(cls):
        UI.clean()
        print("=== Adicionar Item ao Carrinho ===")
        id_prod = int(input("ID do produto a adicionar: "))
        qtd = int(input("Quantidade do produto: "))
        View.produto_inserir_carrinho(id_prod, cls.__usuario.get_id(), qtd)
        print("\nProduto adicionado ao carrinho com sucesso!")
        UI.continuar()

    @classmethod
    def carrinho_listar(cls):
        UI.clean()
        print("=== Meu Carrinho ===")
        itens, total = View.carrinho_listar(cls.__usuario.get_id())
        if itens:
            for i in itens:
                print(
                    f'{i["descricao"]} - Preço: {i["preco_unitario"]:.2f}',
                    f'\tQuantidade: {i["qtd"]} - Total: R$ {i["total_item"]:.2f}',
                    sep="\n",
                )
            print(f"\nValor Total: R$ {total:.2f}")

        else:
            print("\nNão há itens no carrinho.")

        UI.continuar()

    @classmethod
    def carrinho_comprar(cls):
        UI.clean()
        print("=== Confirmar Compra ===")
        itens, total = View.carrinho_listar(cls.__usuario.get_id())
        if itens:
            print(f"\nValor Total da Compra: R$ {total:.2f}")
            op = input("\nDeseja confimar essa compra? N/s ")
            if op.lower() == "s":
                View.carrinho_comprar(cls.__usuario.get_id())
                print("\nCompra confirmada com sucesso!")
                UI.continuar()
            else:
                print("\nConfirmação cancelada.")
                UI.continuar()
        else:
            print("\nNão há items no carrinho.")
            UI.continuar()

    @classmethod
    def compra_listar(cls) -> None:
        UI.clean()
        print("=== Lista de Compras ===", "\n")
        compras = View.compra_listar(cls.__usuario.get_id())
        for c in compras:
            venda, items = c
            print(
                f"Comprado de {venda.get_data().strftime("%d/%m/%Y %H:%M")}",
                f"Valor Total: R$ {venda.get_total():.2f}",
                sep=" - ",
            )
            for i in items:
                print(
                    f"\t{i["descricao"]} ({i["preco_uni"]:.2f})",
                    f"Quant. {i["qtd"]} ({i["preco_qtd"]:.2f})",
                    sep=" - ",
                )
            print()
        UI.continuar()

    def categoria_inserir() -> None:
        UI.clean()
        print("=== Inserir Categoria ===")
        descricao = input("Descrição: ")
        View.categoria_inserir(descricao)
        print(f"Categoria inserida com sucesso!")
        UI.continuar()

    def categoria_listar() -> None:
        UI.clean()
        print("=== Lista de Categorias ===")
        categorias = View.categoria_listar()
        if not categorias:
            print("Nenhuma categoria cadastrada!")
            return
        for categoria in categorias:
            print(categoria)
        UI.continuar()

    def categoria_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Categoria ===")
        id = int(input("ID da categoria a atualizar: "))
        desc = input("Nova descrição: ")
        View.categoria_atualizar(id, desc)
        print(f"Categoria atualizada com sucesso!")
        UI.continuar()

    def categoria_excluir() -> None:
        UI.clean()
        print("=== Excluir Categoria ===")
        id = int(input("ID da categoria a excluir: "))
        View.categoria_excluir(id)
        print(f"Categoria excluída com sucesso!")
        UI.continuar()

    def cliente_listar() -> None:
        UI.clean()
        print("=== Lista de Clientes ===")
        clientes = View.cliente_listar()
        if not clientes:
            print("Nenhum cliente cadastrado!")
            return
        for cliente in clientes:
            print(cliente)
        UI.continuar()

    def cliente_inserir() -> None:
        UI.clean()
        print("=== Inserir Cliente ===")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        fone = input("Fone: ")
        View.cliente_inserir(nome, email, senha, fone)
        print(f"Cliente inserido com sucesso!")
        UI.continuar()

    def cliente_atualizar() -> None:
        UI.clean()
        print("=== Atualizar Cliente ===")
        id = int(input("ID do cliente a atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")
        View.cliente_atualizar(id, nome, email, fone)
        print(f"Cliente atualizado com sucesso!")
        UI.continuar()

    def cliente_excluir() -> None:
        UI.clean()
        print("=== Excluir Cliente ===")
        id = int(input("ID do cliente a excluir: "))
        View.cliente_excluir(id)
        print(f"Cliente excluído com sucesso!")
        UI.continuar()
