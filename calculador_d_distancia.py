
import time
import math
#Calculador de distância de dois pontos em um plano cartesiano.

class ponto:
    def __init__(self):
        self.pontox = 0
        self.pontoy = 0

    def recebendo_coordenadas(self):
        
        while True:
            try:
                self.pontox = float((input("Digite a coodenada x: ")).replace(",", "."))
                self.pontoy = float((input("Digite a coodenada y: ")).replace(",", "."))
                print("Entrada de dados aceita, processando...")    
                time.sleep(2)
                break
            except ValueError:
                print("Valor inválido, tente novamente.")

        
class mapa:
    
    def calculador_distancia(self,medidaUm, medidaDois):
        soma_d_quadrados = (medidaUm.pontox - medidaDois.pontox)**2 + (medidaUm.pontoy - medidaDois.pontoy)**2
        resultado = math.sqrt(soma_d_quadrados)
        print("processando...\n")
        time.sleep(1)
        print(f"\nA distância entre os pontos é: {resultado:.2f}")

print("=-="*2,"calculador simples em plano cartesiano","=-="*2)
medidaA = ponto()
print("-=-"*3,"Ponto A","-=-"*3)
medidaA.recebendo_coordenadas()

medidaB = ponto()
print("-=-"*3,"Ponto B","-=-"*3)
medidaB.recebendo_coordenadas()

meu_mapa = mapa()
meu_mapa.calculador_distancia(medidaA, medidaB)

