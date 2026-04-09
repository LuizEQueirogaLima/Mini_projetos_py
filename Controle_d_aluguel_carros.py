import time

#três classes:
# A primeira é da locadora, que terá a quantidade dos carros.
# A segunda seria a consulta com o cliente
# A terceira é o calculo para saber o valor final da locação

class Locadora:
    def __init__(self):
        self.carros = 0
        # 1° nome do carro, 2° valor 3° quantidades desse veiculo
        self.tipos = {"Hatch": [0,0], "Sedan":[0,0],"SUV":[0,0]}
        
    def  quant_carros(self):
        print("Sistema para controle de locação de carros")
        
        while True:
            try:
    
                self.carros = int(input("Digite a quantidade de carros que a locadora tem:"))
                if self.carros < 0:
                    print("Erro o a quantidade de carros não pode ser negativa, tente de novo...")
                    continue
                elif self.carros > 50:
                    print("Erro, o pátio não comporta a quantidade digitada")
                break
            except ValueError:
                print("Erro! digite um número inteiro")
                
        print("Dados gravados com sucesso!!\n")
        time.sleep(1)
        print("Vamos distribuir a quantidade digitada entre os tipos de veículo ")
        
        time.sleep(1)
        
        while True:
            parcial = 0
            tentativa = 0
            for chave, itens in self.tipos.items():
                while True:
                    try:
                        tentativa = int(input(f"Sobre o carro: {chave}, digite a quantidade qua há em sua loja: "))
                        if parcial + tentativa > self.carros:
                            time.sleep(1)
                            print(f"Erro, distribua a quantidade de carros no sistema de acordo com a quantiadade estipulada: {self.carros} carros\n")
                            continue
                        itens[0] = tentativa
                        parcial += tentativa
                        break
                    except ValueError:
                        print(f"Erro, digite um valor inteiro válido que se encaixe na quantidade de {self.carros}")        
                        
                while True:
                    try:
                        itens[1] = float(input(f"Digite o valor da diaria do carro {chave} R$: ").replace(",","."))
                        if itens[1] < 0:
                            print("Erro, o valor não pode ser negativo, tente de novo")
                            continue
                        break
                    except ValueError:
                        print("Erro, digite um valor positivo para a diaria")
                        
            if parcial < self.carros:
                print("Erro, A distribuição de quantidades no sistema DEVE bater com o número máximo de carros Tente de novo!!\n")
                time.sleep(1)
                continue
            elif parcial == self.carros:
                
                print("Dados registrados!!, excutando próximo programa!!\n")
                time.sleep(2)
                break
              
class Locatario:
    
    def __init__(self):
        self.veiculos = []
        self.carEscolhido = 0
        self.dias = 0
        
    def recebendo(self,dados_locadora):
        print("Sistema de atendimento ao cliente...\nEscolha o tipo de carro que quer alugar\n")

        escolha = 0
        numero_opcao = 0
        for carro, dados in dados_locadora.tipos.items():            
            
            if dados[0] >= 1:
                numero_opcao += 1
                self.veiculos.append(carro)

                print(f"[{numero_opcao}] - O Carro {carro} está disponível (Temos {dados[0]} unidades). Diária R${dados[1]:.2f}")
        while True:                
            try:
                escolha = int(input("Digite a sua escolha: "))
                if 1 <= escolha <=len(self.veiculos):
                    self.carEscolhido = self.veiculos[escolha - 1]
                    print(f"O carro escolhido foi o: {self.carEscolhido}\n")
                    time.sleep(1)
                    
                    while True:
                        try:
                            self.dias = int(input("Por quantos dias gostaria de ficar com o carro?"))
                            time.sleep(1)
                            if self.dias < 0:
                                print("A quantidade de dias solicitada deve ser maior que zero\n")
                                time.sleep(1)
                                continue
                            break
                        except ValueError:
                            print("Erro: valor inválido!!\n")
                    time.sleep(1)
                    break
                else:
                    print ("Erro: digite uma das opções que há no menu..\n")
                    time.sleep(1)
                
            except ValueError:
                print("informação invália! escolha uma das opções a cima\n")
                
class Calculador:
    
    def funCalculadora(self,dados_locadora,clienteA):
        carro = ""
        valor_final = 0
        print("Iniciando o sistema de calculo...\n")
        time.sleep(2)
        carro = clienteA.carEscolhido

        valor_final = dados_locadora.tipos[carro][1] * clienteA.dias
        print(f"\nDados finais da locação:\nO cliente alugou um carro do tipo: {clienteA.carEscolhido}\nFoi alugado por {clienteA.dias}dias.\nO valor final ficou em R${valor_final:.2f}")
        time.sleep(2)
        print("Fim do programa!!")
        time.sleep(2)
        
dados_locadora = Locadora()
dados_locadora.quant_carros()
clienteA = Locatario()
clienteA.recebendo(dados_locadora)
calcular = Calculador()
calcular.funCalculadora(dados_locadora,clienteA)

