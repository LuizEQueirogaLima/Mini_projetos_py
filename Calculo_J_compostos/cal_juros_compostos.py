#Projeto calculador de Juros comp >  página de calculo
import time

class Investimento:

    def __init__(self,capital,taxa,temp_ini):
        self.capital_inicial = capital
        self.taxa_mensal = taxa
        self.tempo = temp_ini

        
    def calculadora_de_taxas(self):
        capital_calculado = self.capital_inicial
        taxa_real = self.taxa_mensal / 100
        
        for i in range (1,self.tempo+1):
            capital_calculado = capital_calculado + capital_calculado * taxa_real
        
        print('Calculo Feito')
        time.sleep(1)
        print(f"valor estimado ao longo de {self.tempo} Mês(s) é de: R${capital_calculado:.2f}","\n")
        
        print(f"o calculo foi feito com base na taxa de Calculo: {self.taxa_mensal}%")







