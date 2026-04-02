import time
class Tabuada:

    def __init__(self):
        self.num_inicial = 0
        self.num_final = 0
    
    print("==="*7,"Sistema de Tabuada personalizada","==="*7)

    def Entrada_valores(self):
        print('\n',"=="*5,"Digite o valor inicial e o valor final para o calculo","=="*5)
        time.sleep(1)
        while True:
            try:
                self.num_inicial = int(input("Digite o 1° número do Loop: "))
                self.num_final = int(input("Digite o 2° número do loop: "))
                if self.num_inicial > self.num_final:
                    print("Erro.. número inicial deve ser maior que o número final\n Tente de novo")
                    time.sleep(1)
                    continue
                print("Dados gravados...\nCalculando...")
                time.sleep(1)
                break

            except ValueError:
                print("Valor de Entrada incorreto, digite um valor inteiro para o calculo")
        return (self.num_inicial,self.num_final)
    
    def calculador(self,inicial,final):

        resultados_final = {}
        for cont in range (inicial, final+1, 1):
            resultados_parcial = []
 
            for i in range (1,11,1):
                resultados_parcial.append(cont * i)
            resultados_final[cont] = resultados_parcial

        return (resultados_final)
    
    def imprimir(self,resultados_final):
        for chave, elementos in resultados_final.items():
            time.sleep(1)
            print('\n',"=="*5,f"Tabuada do {chave}","=="*5)
            time.sleep(1)
            Val_tabuada = 0 
            for valor in elementos:
                Val_tabuada += 1
                print(f"{chave} * {Val_tabuada} = {valor}")


while True:
    tabuada_per = Tabuada()
    inicial, final = tabuada_per.Entrada_valores()
    resultados_final = tabuada_per.calculador(inicial,final)
    tabuada_per.imprimir(resultados_final)
    print("=="*5,"Aperte qualquer tecla para continuar no programa", "=="*5)
    continuar = input("caso não queria continuar digite [N]: ").strip().upper()
    if continuar == "N":
        break
print("Fim do programa!!")


