import time
import math

#Sistema calculador de área para pintura

# Passo 1: Analisar quantidade e tamanhos diferentes de paredes
# Passo 2: Entrada de Altura, largura 
# Passo 3: Tamanho da lata (litros) e Rendimento por litro
# Passo 4: Calcular com base nas informações recebidas

class Parede:
    def __init__(self):
        self.lista_d_paredes = {} # Dicionário para paredes de tamanho diferente
        self.medidas = [] # Lista para paredes de tamanho igual
        self.p_Tamanho_diferente = False
    
    def quantidade_d_paredes (self):
        quant_paredes = 0
        while True:
            quant_paredes = input("Digite a quantidade de paredes: ")
            if quant_paredes.isdigit():
                quant_paredes = int(quant_paredes)
                if quant_paredes > 10:
                    print("quantidade muito grande de paredes para serem calculadas\nPorfavor coloque uma quantidade a baixo de 10")
                    continue
                print("Registrado!!\n")
                time.sleep(1)
                break
            else:
                print("Erro, o valor digitado deve ser inteiro para que seja feita a análise")
    
        return quant_paredes
    
    def info_parede (self,quant_paredes):
        print("Atribuindo valores da parede\n")
        verifica_as_paredes = " "
        while True:
            if quant_paredes > 1:
                verifica_as_paredes = input("todas as paredes são do mesmo tamanho [S] Sim / [N] Não:").upper()
            else:
                verifica_as_paredes = "S"
                
            if verifica_as_paredes == "S":
                while True:
                    try:
                        self.medidas.append(
                            float(input("Digite a altura da parede: ").replace(',','.')))
                        self.medidas.append(
                            float(input("Digite a largura da parede: ").replace(',','.')))
                        self.medidas.append(quant_paredes)
                        print("\n","  "*10,"Informações registradas!!","  "*10,"\n")
                        time.sleep(1)

                        self.p_Tamanho_diferente = False
                        break
                    
                    except ValueError:
                        print("Erro, uma das informações foi inválida, digite novamente\n")
                        time.sleep(1)
                break
            elif verifica_as_paredes == "N":
                print("As paredes são de tamanhos diferentes\n")
                medidas = []
                for cont in range (quant_paredes):
                    while True:
                        try:
                            medidas.append(
                                float(input("Digite a altura da parede: ").replace(',','.')))
                            medidas.append(
                                float(input("Digite a largura da parede: ").replace(',','.')))
                            print("\n","  "*10,"Informações registradas!!","  "*10,"\n")
                            
                            self.lista_d_paredes[cont] = medidas
                            time.sleep(1)
                            break
                        except ValueError:
                            print("Erro, uma das informações foi inválida, digite novamente")
                self.p_Tamanho_diferente = True
                break
            else:
                print("Erro... você deve digitar [S] para sim ou [N] Para Não\n")
        
class TipoTinta:
    def __init__(self):
        self.rendiment_p_litro = 0
        self.volume = 0

    def tinta_gasta (self):
        while True:
            try:
                self.volume = float(input("Digite o volume de litros da lata de tinta: ").replace(',','.'))
                self.rendiment_p_litro = float(input("Digite o volume de rendimento da tinta: ").replace(',','.'))
                print("Informações registradas")
                time.sleep(1)
                break
            except ValueError:
                print("Erro, uma das informações foi inválida, digite novamente\n")
                time.sleep(1)
            
class Calculador:
    def __init__(self):
        self.quantlatas = 0
    
    def calcular (self):
        if minha_parede.p_Tamanho_diferente == True: 
            area_total = 0
            contador_das_paredes = 0

            for indice, info in minha_parede.lista_d_paredes.items():# ver esse indice
               
                area_total += info[0] * info[1]
                contador_das_paredes += 1
                
            print("\nCalculando informações\n")
            time.sleep(1)
            
            print(f"Foram {contador_das_paredes} paredes de tamanhos diferentes, segue status completo de calculo.\n")
            time.sleep(1)
            self.otimizacao(area_total)
            
        elif minha_parede.p_Tamanho_diferente == False:
            area_total = 0


            if minha_parede.medidas[2] > 1:
                time.sleep(1)
                print(f"\nTendo a quantidade de paredes: {minha_parede.medidas[2]}, segue o calculo\n")
                time.sleep(1)
            else:
                time.sleep(1)
                print("\nTendo a somente uma parede para medida, segue o calculo\n")
                time.sleep(1)
            

            area_total = minha_parede.medidas[0] * minha_parede.medidas[1] * minha_parede.medidas[2]
             
            self.otimizacao(area_total)

            
    def otimizacao (self,area_total):
            sobra_em_litros = 0
            quant_latas = 0
            capacidade_d_compra = 0
            
            quant_latas = math.ceil(area_total / (tinta_d_parede.volume * tinta_d_parede.rendiment_p_litro))
        
            capacidade_d_compra = quant_latas * (tinta_d_parede.volume * tinta_d_parede.rendiment_p_litro)

            sobra_em_litros = (capacidade_d_compra - area_total) / tinta_d_parede.rendiment_p_litro
            
            print(f"Minha área total é de {area_total:.2f}M²\n")
            print(f"A quantidade de latas que você precisa são: {quant_latas} unidades\n")
            print(f"Com essa quantidade você pode pintar {capacidade_d_compra:.2f}M² de área\n")
            print(f"Com a sobra de {sobra_em_litros:.2f} Litros, você conseguiria pintar {capacidade_d_compra- area_total:.2f} m²\n\n")
            time.sleep(2)


        
print("=-="*15,"Programa simples calculador","=-="*15)
minha_parede = Parede()
quant_paredes = minha_parede.quantidade_d_paredes()
minha_parede.info_parede(quant_paredes)

tinta_d_parede = TipoTinta()
tinta_d_parede.tinta_gasta()

inp_calculo = Calculador()
inp_calculo.calcular()

