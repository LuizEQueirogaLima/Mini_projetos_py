from entrada_d_dados import coleta_de_dados

from cal_juros_compostos import Investimento
print()
print(5*"-=-","Programa simples calculador de Juros Compostos", 5*"-=-")

capital_ini, taxa_juros, t_meses = coleta_de_dados()

calcular_investimento = Investimento(capital_ini,taxa_juros, t_meses)

calcular_investimento.calculadora_de_taxas()
