import time
#Desafio, conversor simples de números inteiros para binários.

class ConversorBinario:
    def __init__(self):
        self.inteiro = 0
    
    
    def entrada_d_usuario(self):
        print("-=-"*8,"Verificador simples de números binários","-=-"*8)
        print("   "*2,"O programa converterá números inteiros por dois para achar o formato binário","   "*2)

        while True:
            try:
                num_entrada = int(input("digite o número para a consulta: "))
                if num_entrada < 0:
                    print("processando...\n")
                    time.sleep(1)
                    print("Erro... o valor digitado deve ser maior do que zero...")
                    continue
                elif num_entrada == 0:
                    print("processando...\n")
                    time.sleep(1)
                    print("Erro, o valor digitado não pode ser igual a zero...\n")
                else:
                    return num_entrada
                
            except ValueError:
                print("por favor, digite um número que seja no formato inteiro para continuar")
                
    def convertendo(self,num_entrada):
        print("\nCalculando...\n")
        time.sleep(1)
        
        resto_div = 0
        dic_resultado = {}
        
        while num_entrada > 0:
            resto_div = num_entrada % 2
            num_entrada = num_entrada // 2
            
            print(f"O valor da divisão é de: {num_entrada}","\n")
            print(f"O valor resto é de: {resto_div}\n")
            dic_resultado[num_entrada] = resto_div
            time.sleep(1)

 
        return dic_resultado
    
    def invertendo_binario(self,dic_resultado):
        print("==="*5,"Invertendo o número","==="*5,"\n")
        resultado_binario = []
        for div, res in reversed (dic_resultado.items()):
            resultado_binario.append(res)
            print(f"Resultado de divisão: {div} com resto de: {res}","\n")
            time.sleep(1)
        
        binario_formatado = ''.join(str(numero) for numero in resultado_binario)
        print(f"O resultado binário do número é: {binario_formatado}")
        time.sleep(1)
        print("Encerrando o programa...")
        

conversor = ConversorBinario()
num_entrada = conversor.entrada_d_usuario()
dic_resultado = conversor.convertendo(num_entrada)
conversor.invertendo_binario(dic_resultado)
