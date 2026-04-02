import time

# Sistema para lista de convidados
# 1° Entrada de "lista" de convidados
# 2° Verificação pelo porteiro, ele recebe o nome do convidado e retorna verdadeiro ou falso para o usuário.
# 3° Caso seja verdadeiro, o nome é acrescentado a uma lista de convidados já presentes na festa, caso o nome seja digitado de novo, o porteiro apontará que o convidado já está presente.
# 4° O sistema fica em loop, até que todos os nomes da lista estejam presentes.

class lista_convidados:
    def __init__(self):
        self.lista_convidados = []
    
    def recebendo_nomes(self):
        contador = 0
        while True:
            contador += 1
            nome_de_convidado = input(f"Digite o nome do convidado n°{contador}: ")
            verifica_nome = nome_de_convidado.replace(" ", "")
            if verifica_nome.isalpha():
                print("processando entrada...\n")
                time.sleep(1)
                if nome_de_convidado.upper() in self.lista_convidados:
                    print("Convidado já está nos nomes da festa, porfavor digite outro nome...")
                    contador -= 1
                    continue
                self.lista_convidados.append(nome_de_convidado.upper())
                
                if len(self.lista_convidados) >= 5:
                    print(f"Temos a quantidade de {len(self.lista_convidados)} nomes para a festa.\n\nDeseja continuar a dar entrada em mais nomes?")
                    resposta = input("Digite [S] para sim ou [N] para não:").strip().upper()
                    print("Processando a resposta...\n")
                    time.sleep(1)
                    
                    if resposta == "N":
                        print("Encerrando a entrada de nomes..")
                        break
                    
                    elif resposta == "S":
                        print("Continuando com a entrada de nomes..")
                        time.sleep(1)
                    else:
                        print("resposta inválida... Continuando com a entrada de nomes...")                    
                        time.sleep(1)
            else:
                print("Entrada de nome inválido, por favor, digite um nome válido para a lista")
                contador -= 1


class festa:
    def __init__(self):
        self.convidados_em_festa = []
        
    def convidado (self, lista_da_prancheta):
        verificador = " "
        print("Processando convidados da festa...\n")
        time.sleep(1)
        print(f"Existem n°{len(lista_da_prancheta)} de convidados na lista de presença")
        time.sleep(1)
        print("Recebendo os convidados...\n")
        time.sleep(1)
        while True:
            Nome_real = input("Digite o nome do convidado: ").strip().upper()
            verificador = Nome_real.replace(" ","")
            if verificador.isalpha():
                if Nome_real in lista_da_prancheta: 
                    if Nome_real in self.convidados_em_festa:
                        time.sleep(1)
                        print(f"O convidado: {Nome_real} em questão já está na festa, por favor digite um nome válido\n")
                        continue
                    print(f"Confirmado!! Participante da festa {Nome_real} registrado\n")
                    time.sleep(1)
                    self.convidados_em_festa.append(Nome_real)
                else:
                    print(f"O nome do convidado, {Nome_real} não está na lista!!\nPorfavor digite um nome válido!!\n")
                    time.sleep(1)
                
                if len(self.convidados_em_festa) == len(lista_da_prancheta):
                    print("Atenção!! Número de convidados é igual ao número de participantes da festa, programa encerrando!!\n")
                    time.sleep(1)
                    break
            else:
                print("Informação inválida!!, digite um nome válido")
    
        
        
print("=-="*3,"Controle de convidados","=-="*3)

convidados = lista_convidados()
convidados.recebendo_nomes()

recebendo_convidados = festa()
recebendo_convidados.convidado(convidados.lista_convidados)

