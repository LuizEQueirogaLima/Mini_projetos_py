import time
import random as rs
import string
import msvcrt

# Mini_projeto Baseado na estrutura FIFO
class filaBanco:


    def __init__(self):
        self.cliente_nome = " "
        self.cliente_idade = 0
        self.lista_d_clientes = {}


    def entrada_d_clientes(self):
        contador = 0
        verifica_clientes_restantes = ""

        print("==="*20,"Programa simples de banco","==="*20,"\n")
        while True:
            informacoes_cliente_parcial = []
            contador += 1

            while True:
                self.cliente_nome = input("Digite o nome do cliente: ")
                verifica_cliente = self.cliente_nome.replace(" ", "")

                if verifica_cliente.isalpha(): #verifica se existem caracteres especiais na entrada
                    time.sleep(1)
                    informacoes_cliente_parcial.append(self.cliente_nome)
                    break
                else:
                    time.sleep(1)
                    print("\nErro, o nome de cliente não pode ter caracteres especiais, nem números\n\nPorfavor digite o nome novamente!")

            while True: 
                try:
                    self.cliente_idade = int(input(f"Digite a idade do cliente {self.cliente_nome}: "))
                    informacoes_cliente_parcial.append(self.cliente_idade)
                    break
                except ValueError:
                    print("\nErro... digite uma idade em formato inteiro.")

            letra_d_senha = rs.choice(string.ascii_uppercase)
            Senha_d_chegada = f"{letra_d_senha}-{contador:02d}"
            self.lista_d_clientes[Senha_d_chegada] = informacoes_cliente_parcial

            print("\nExiste outro cliente para entrar na fila?")
            print("\nDigite qualquer tecla para continuar ou digite (N) para parar com a entrada de clientes: ")
            verifica_clientes_restantes = msvcrt.getch().lower()

            if verifica_clientes_restantes == b'n':
                print("processando...", end=" ")
                time.sleep(1)
                print("Encerrando a entrada de clientes..")
                time.sleep(1)
                break
            else:
                print("processando...", end=" ")
                time.sleep(1)
                print("continuando com a entrada de clientes...\n")
                time.sleep(1)

    def atendimento_clientes(self):
        nome_d_cliente = " "
        idade_d_cliente = 0
        fila_especial = 0


        print("segue lista de clientes a serem atendidos: \n")
        for senha, cliente in self.lista_d_clientes.items():
            nome_d_cliente = cliente[0]
            idade_d_cliente = cliente[1]

            print(f"Senha: {senha} / Nome: {nome_d_cliente}/ Idade: {idade_d_cliente}\n")
            time.sleep(1)

            if idade_d_cliente >= 60:
                fila_especial += 1

        if fila_especial > 0: 
            time.sleep(1)
            print(f"Clientes a cima dos 60: {fila_especial}")
        
        print("\n","Fim do programa!!")
            

        




gerenciador_banco = filaBanco()

gerenciador_banco.entrada_d_clientes()
gerenciador_banco.atendimento_clientes()



