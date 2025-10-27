from clienteDAO import ClienteDAO
from cliente import Cliente
import os


class UI:
    @staticmethod
    def main() -> None:
        ClienteDAO.abrir()
        while True:
            # limpa o terminal (Windows -> 'cls', Unix -> 'clear')
            # os.system("cls" if os.name == "nt" else "clear")
            print("=" * 30)
            op = UI.menu()
            print("=" * 30)
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
            else:
                print("Opção inválida!")

    def menu() -> int:
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Sair")
        return int(input("Escolha uma opção: "))

    def cliente_listar() -> None:
        clientes = ClienteDAO.listar()
        if not clientes:
            print("Nenhum cliente cadastrado!")
            return
        for cliente in clientes:
            print(cliente)

    def cliente_inserir() -> None:
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.inserir(cliente)
        print(f"Cliente {cliente.get_nome()} inserido com sucesso!")

    def cliente_atualizar() -> None:
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

    def cliente_excluir() -> None:
        id = int(input("ID do cliente a excluir: "))
        cliente = ClienteDAO.listar_id(id)
        if cliente is None:
            print("Cliente não encontrado!")
            return
        ClienteDAO.excluir(cliente)
        print(f"Cliente {cliente.get_nome()} excluído com sucesso!")
