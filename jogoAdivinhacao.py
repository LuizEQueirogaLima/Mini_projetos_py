import time
import random as rn

class JogoAdivinhacao:

    def __init__(self):
        self.jogador = 0
        self.numero_da_maquina = 0

    def mensagem_inicial(self):
        print("="*15,"Mini jogo de advinhação","="*15)
        print("  "*5,"Adivinhe um número entre 1 a 100","  "*5)
        time.sleep(1)

        
    def jogada_d_maquina(self):
        self.numero_da_maquina = rn.randint(1, 100)

    def jogada(self):
        self.jogador = 0
        while True:
            try:
                self.jogador = int(input("Tentativa: "))
                if self.jogador < 1 or self.jogador > 100:
                    print("\npor favor digite um valor entre 1 a 100")
                    continue
                break
            except ValueError:
                print("Erro, entrada inválida\n",'  ' *5,"Digite um número inteiro entre 1 e 100",'  ' *5)
                time.sleep()
        
    def partida(self):
        numero_primo = True
        diferenca = abs(self.numero_da_maquina - self.jogador)
        #print(self.numero_da_maquina)
        
        if self.numero_da_maquina == self.jogador:
            print("Você acertou o número!!")
            time.sleep(1)
            print("Fechando o programa!!!")
            time.sleep(1)
            return True 

        if diferenca % 2 == 0:
            print("Dica número um: A diferença entre os números gera um número Par!!")
        else:
            print("Dica Número um: A diferença entre os números gera um número Ímpar!!")
            
        if diferenca == 1:
            print("Dica número dois: A diferença entre os dois números gera um número que não é primo!!")
        else:
            for i in range(2, diferenca):
                if diferenca % i == 0:
                    numero_primo = False
                    break
                    
            if numero_primo:
                print("Dica numero dois: A diferença entre os dois números gera um número Primo!!")
            else:
                print("Dica número dois: A Diferença entre os dois números gera um número que não é primo!!")
                
        print("\n", "=-="*4, "Tente de novo!!", "=-="*4)

jogo = JogoAdivinhacao()
jogo.mensagem_inicial()
jogo.jogada_d_maquina()

jogo_vencido = False
while not jogo_vencido:
    jogo.jogada()
    jogo_vencido = jogo.partida()