import time
import random as rn

finalizado = True

class jogoAdivinhacao:

    def __init__(self):
        self.jogador = 0

    def mensagem_inicial(self):
        print("="*15,"Mini jogo de advinhação","="*15)
        print("  "*5,"Adivinhe um número entre 1 a 100","  "*5)

    def jogada(self):

        while True:
            try:
                self.jogador = int(input("Tentativa: "))
                if self.jogador < 1 or self.jogador > 100:
                    print("\npor favor digite um valor entre 1 a 100")
                    continue
                break
            except ValueError:
                print("Erro, entrada inválida\n",'  ' *5,"Digite um número inteiro entre 1 e 100",'  ' *5)
                time.sleep(1)
        return(self.jogador)
    
    def jogada_d_maquina(self):
        numero_d_maquina = rn.randint(1, 100)
        return(numero_d_maquina)
    
    def partida(self,numero_d_maquina, resultado_tentativa):
        while True:
            numero_do_usuario_maior = 0
            numero_do_usuario_menor = 0
            numero_primo = True
            finalizado = True
            #print(f"jogada da maquina: {numero_d_maquina}")

            if resultado_tentativa > numero_d_maquina:
                numero_do_usuario_maior = resultado_tentativa - numero_d_maquina

                if numero_do_usuario_maior % 2 == 0:
                    print("\nDica número um: A difernça entre os números gera um número Par!!")
                else:
                    print("\nDica Número um: A diferença entre os dos números, gera um número ímpar!!")
                
                for i in range (2, numero_do_usuario_maior):
                    if numero_do_usuario_maior % i == 0:
                        print("\nDica número dois: A Diferença entre os dois números gera um número que não é primo!!")
                        numero_primo = False
                        break

                if numero_primo:
                    print("\nDica numero dois: A diferença entre os dois números gera um número Primo!!")

                print("\n","=="*5,"Tente de novo!!","=="*5)
                resultado_tentativa = self.jogada()

            elif numero_d_maquina > resultado_tentativa:
                numero_do_usuario_menor = numero_d_maquina - resultado_tentativa

                if numero_do_usuario_menor % 2 == 0:
                    print("\nDica número um: A difernça entre os números gera um número Par!!")
                else:
                    print("\nDica Número um: A diferença entre os dos números, gera um número ímpar!!")
                
                for i in range (2, numero_do_usuario_menor):
                    if numero_do_usuario_menor % i == 0:
                        print("\nDica número dois: A Diferença entre os dois números gera um número que não é primo!!")
                        numero_primo = False
                        break
                if numero_primo:
                    print("\nDica numero dois: A diferença entre os dois números gera um número Primo!!")
                print("\n","=="*5,"Tente de novo!!","=="*5)
                resultado_tentativa = self.jogada()

            elif numero_d_maquina == resultado_tentativa:
                print("Você acertou o número!!")
                time.sleep(1)
                print("fechando o programa!!!")
                time.sleep(1)
                finalizado = False
                break
        return(finalizado)
        
while finalizado:

    jogo = jogoAdivinhacao()
    jogo.mensagem_inicial()
    numero_d_maquina = jogo.jogada_d_maquina()
    resultado_tentativa = jogo.jogada()
    finalizado = jogo.partida(numero_d_maquina,resultado_tentativa)
