import time

#calculador de IMC usando classe

# CALCULO IMC: peso / (altura X altura)

#CLASSIFICAÇÃO
# Menor que 18,5	Magreza	0
#Entre 18,5 e 24,9	Normal	0 
#Entre 25,0 e 29,9	Sobrepeso	I
#Entre 30,0 e 39,9	Obesidade	II
#Maior que 40,0	Obesidade Grave	III

class AvaliadorImc:
    def __init__(self):
        self.pacientes = {}
        self.meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","setembro","Outubro","Novembro","Dezembro"]
        
    def info_d_usuario(self):
        quantidade = 0
        print("=-="*5,"Calculador progressivo de peso do usuário","=-="*5)
        while True:
            try:
                quantidade = int(input("Digite a quantidade de participantes a serem avaliados: "))    
                if quantidade < 0:
                    print("Erro, entrada inválida, digite um número que seja positivo para a verificação")
                    continue
                elif quantidade == 0:
                    print("Erro, digite um número que seja maior que zero")
                    continue
                elif quantidade > 10:
                    print("Quantidade muito longa.. só é permitido a esse programa, a quantidade máxima de Dez pessoas por execução")
                    continue
                break
            except ValueError:
                print("Erro, digite um valor que seja inteiro.")
                
        for quant in range (0,quantidade,1):
            peso = 0
            altura = 0
            progressivo = 0
            pacientes_info = []
            while True:    
                try:
                    print()
                    altura = float((input(f"Digite a altura do paciente: ")).replace(",", "."))
                    if altura <=0:
                        print("\nA altura não pode ser menor ou igual a zero\npor favor Tente de novo..")
                        time.sleep(1)
                        continue
                    peso = float((input(f"Digite o peso do paciente n°{quant+1}: ")).replace(",", "."))
                        
                    progressivo = int(input("Digite a progressão em volume de peso que o paciente terá: "))
                    time.sleep(1)
                    pacientes_info.append(peso)
                    pacientes_info.append(altura)
                    pacientes_info.append(progressivo)
                    break
                except ValueError:
                    print("Erro, uma das informaçoes foram digitadas da forma errada, porfavor, tente de novo")
            self.pacientes[quant] = pacientes_info
        
        print("\n","Entrada de pacientes fechada, indo para a próxima etapa\n")
    
    def avaliador_d_peso(self):
        print("\n","=-="*5,"Avaliando os pacientes","=-="*5,"\n")
        for numero, paciente in self.pacientes.items():
            cres_decrescent = 0
            while True:
                try:
                    print(f"Para o paciente de número {numero+1} temos as sequintes opções:","\n[1] Calcular o peso de forma crescente ","\n[2] Calcular o peso de forma decrescente\n")
                    cres_decrescent = int(input(f"O que gostaria de fazer? "))
                    if cres_decrescent == 1:
                        time.sleep(1)
                        print("foi escolhido a forma ganhando peso...\nCalculando o peso esperando para o inicio até o fim do ano...\n")
                        time.sleep(1)
                        
                        for i in range (1,12+1,1):
                            paciente[0] = paciente[0] + paciente[2]
                            print(f"No mês de: {self.meses[i-1]} seria de:{paciente[0]:.1f}Kg\n")
                            time.sleep(1)
                        break
                    elif cres_decrescent == 2:
                        print("foi escolhido a forma de perder peso...\nCalculando o peso esperando para o inicio até o fim do ano...\n")

                        for i in range (1,12+1,1):
                            paciente[0] = paciente[0] - paciente[2]
                            print(f"No mês de: {self.meses[i-1]} seria de:{paciente[0]:.1f}Kg\n") # ele não passa para o próximo item do dicionário e não pula a lista, lop infinito
                            time.sleep(1)
                        break
                except ValueError:
                    print("Erro, Você deve entre as opções 1 e 2 para continuar.")
    
    def calcular_imc(self):
        imc_calculado = 0
        print("\n","=-="*5,"Calculando o IMC de cada paciente","=-="*5,"\n")
        time.sleep(1)
        for numero, paciente in self.pacientes.items():
            imc_calculado = paciente[0] / (paciente[1]*paciente[1])
            print(f"Paciente número: {numero+1}")
            print(f"O IMC é: {imc_calculado:.2f}")
            if imc_calculado < 18.5:
                print(f"O paciente teria o peso de: {paciente[0]:.1f}Kg\nEle com a altura: {paciente[1]:.2f}M\nO indice corporal seria de: {imc_calculado:.2f} IMC, estando na categoria de subnutrido\nTipo 0\n")
            elif imc_calculado >= 18.5 and imc_calculado <= 24.9:
                print(f"O paciente teria o peso de: {paciente[0]:.1f}Kg\nEle com a altura: {paciente[1]:.2f}M\nO indice corporal seria de: {imc_calculado:.2f} IMC, estando na categoria normal de peso\nTipo 0\n")
            elif imc_calculado >= 25.0 and imc_calculado <= 29.9:
                print(f"O paciente teria o peso de: {paciente[0]:.1f}Kg\nEle com a altura: {paciente[1]:.2f}M\nO indice corporal seria de: {imc_calculado:.2f} IMC, estando sobrepeso\nTipo 1\n")
            elif imc_calculado >= 30.0 and imc_calculado <= 39.9:
                print(f"O paciente teria o peso de: {paciente[0]:.1f}Kg\nEle com a altura: {paciente[1]:.2f}M\nO indice corporal seria de: {imc_calculado:.2f} IMC, estando na categoria de obesidade\nTipo 2\n")
            elif imc_calculado > 40:
                print(f"O paciente teria o peso de: {paciente[0]:.1f}Kg\nEle com a altura: {paciente[1]:.2f}M\nO indice corporal seria de: {imc_calculado:.2f} IMC, estando na categoria de Obesidade Grave\nTipo 3\n")

calculador = AvaliadorImc()
calculador.info_d_usuario()
calculador.avaliador_d_peso()
calculador.calcular_imc()

