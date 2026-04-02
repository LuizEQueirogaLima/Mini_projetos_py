import time
#Projeto calculador de Juros compostos, entrada

def coleta_de_dados():
    time.sleep(2)
    print("\n",10*"   ",">> ENTRADA DE DADOS <<",10*"   ","\n")
    while True:
        try:
            capital_inicial = float(input("Digite o valor de patrimônio inicial: ").replace(",", "."))
            taxa_juros = float(input("digite o valor da taxa de juros mensal: ").replace(",", "."))
            if taxa_juros > 100 or taxa_juros < 0.1:
                print(5*"  ","ERRO!!",5*"  ","\n")
                time.sleep(1)
                print(" "*2,">>","Sua entrada para Calculo de Juros compostos deve começar entre 0,1 até 100%","<<"," "*2)
                time.sleep(1)
                print("\n Digite novamente um número que atenda esse requisito, não é preciso adicionar o simbolo de %","\n")
                
                continue
            tempo_p_mes = int(input("Digite a quantidade de meses para que seja feito o calculo: "))
            
            
            break
        except ValueError:
            print(5*"  ","ERRO!!",5*"  ","\n")
            print(" "*2,">>","Verifique se a entrada de informação está correta","<<"," "*2)
            time.sleep(1)
            print("\n","Usaremos nesse calculo dois números de ponto flutuante e um inteiro (O inteiro é a quantidade de meses)")
            print("\n","Verifique novamente e tente de novo.","\n")
            time.sleep(1)
            

    return capital_inicial, taxa_juros, tempo_p_mes
