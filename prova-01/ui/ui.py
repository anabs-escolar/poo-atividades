from datetime import datetime, timedelta
from ..dao import PessoaDAO, CorridaDAO
from ..models import Pessoa, Corrida

class UI:

    @staticmethod
    def main() -> None:
        PessoaDAO.abrir()
        CorridaDAO.abrir()
        UI.menu()

    @staticmethod
    def menu() -> None:
        while True:
            print("===== Treinos de Corridas =====")
            print("1. Inserir Pessoa")
            print("2. Listar Pessoas")
            print("3. Pesquisar Pessoas")
            print("4. Inserir Corrida")
            print("5. Listar Corrida")
            print("6. Corrida com Menor Pace")
            print("0. Sair")

            op = int(input("\nEscolha uma opção: "))
            if op == 1:
                UI.pessoa_inserir()
            elif op == 2:
                UI.pessoa_listr()
            elif op == 3:
                UI.pessoa_pesquisar()
            elif op == 4:
                UI.corrida_inserir()
            elif op == 5:
                UI.corrida_listar()
            elif op == 6:
                UI.corrida_menor_pace()
            elif op == 0:
                break 
            else:
                continue

    
    def pessoa_inserir():
        id = int(input("ID: "))
        nome = input("Nome: ")
        n = input("Nascimento (dd/mm/AAAA): ")
        nasc = datetime.strftime(n, "%d/%m/%Y")
        PessoaDAO.inserir(Pessoa(id, nome, nasc))


    def corrida_inserir():
        id = int(input("ID: "))
        t = input("Tempo (HH:MM:ss): ")
        dist = int(input("Distancia em Km: "))

        t = map(int, t.split(":"))
        tempo = timedelta(hours=t[0],minutes=t[1],seconds=t[2])

        d = input("Data (dd/mm/AAAA): ")
        data = datetime.strftime(d, "%d/%m/%Y")

        print("Lista de Pessoas")
        for i in PessoaDAO.listar():
            print("\t",i)

        id_p = int(input("\nID da Pessoa: "))
        CorridaDAO.inserir(Corrida(id, id_p, data, dist, tempo ))

    def pessoa_listar():
        print("Lista de Pessoas")
        for i in PessoaDAO.listar():
            print("\t",i)
    
    def corrida_listar():
        print("Lista de Corridas")
        for i in PessoaDAO.listar():
            print("\t",i)

    def pessoa_pesquisar():
        n = input("Pesquise um nome: ").lower

        print("Resultados")
        for i in PessoaDAO.listar():
            if i.get_nome().lower in n:
                print(i)
