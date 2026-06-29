import time
import re

class ContaBanco:
        def __init__(self):
            self.agencia = "001" 
            self.nome = ""
            self.senha = 0
            self.saldo = 0
            self.limCartao = 0
            self.limiteusado = 0
        
        def Criausuario(self): 
            
            while True:
                Srt_completo = True
                self.nome = input("Digite o nome do usuário: ")
                verificadorNome = self.nome.replace(" " , "")
                for letra in verificadorNome:
                    if letra.isdigit():
                        print("Erro, o nome de usuário não pode conter números, porfavor, escreva o nome do usuário")
                        Srt_completo = False
                        break
                if re.search (r'[^a-zA-Z0-9 ]', verificadorNome): # caracteres especiais
                        print("Erro, o usuário não pode ter caracteres especiais, tente novamente")
                        Srt_completo = False
                        continue
                    
                if Srt_completo == True:  
                    break
            
            while True:
                try:

                    self.senha = int(input(f"Agora vamos criar a senha do usuário {self.nome}: "))
                    if len(str(self.senha)) != 6:
                        print("Erro, a senha deve ter o tamanho de exatos SEIS digitos\n")
                        continue
                    if self.senha < 0:
                        time.sleep(1)
                        print("Erro, a senha não pode ter números negativos...\n")
                        continue
                    break
                
                except ValueError:
                    time.sleep(1)
                    print("Erro, digite números inteiros para o cadastro da senha de cliente...\n")
                    time.sleep(1)
                
            while True:
                try:    
                    self.saldo = float((input("Diga o valor depositado no ato da criação da conta: R$ ")).replace(",","."))
                    print()
                    self.limCartao = float((input("Diga o limite de cartão inicial do usuário: R$ ")).replace(",","."))
                    if self.saldo <= 0 or self.limCartao <= 0:
                        print("Os valores digitados não podem ser menores ou iguais a zero")
                        time.sleep(1)
                        continue
                    break
                except ValueError:
                    print("Erro, digite um número para saldo e limite de cartão.\n")
            time.sleep(1)
            print(f"\nDados registrados!!\nUsuário {self.nome}\nSua agencia é a n°:{self.agencia}\nSua senha é: {self.senha}\nO saldo da sua conta é R$ {self.saldo:.2f}\nO limite estipulado do seu cartão é de R$ {self.limCartao:.2f}")
            time.sleep(2)

class EscPagamento:
    
    def puxarpagamento (self):
        opcoes = {1:"PIX",2:"CRÉDITO",3:"DEBITO"}
        pagescolha = 0
        print('Sistema de pagamento do banco ativado!! escolha a forma de pagamento\n')
        while True:
            try:
                print("[1] ------ PIX\n[2] ------ CRÉDITO\n[3] ------ DEBITO")
                pagescolha = int(input("Escolha: "))
                if 1 <= pagescolha <= 3:
                    for num, pag in opcoes.items():
                        if pagescolha == num:
                            print(f"Forma de pagamento escolhida foi {pag}\n")
                            time.sleep(1)
                            return num, pag
                else:
                    print("Erro, por favor escolha uma opção válida do menu")
                    time.sleep(1)
            except ValueError:
                print("Erro... digite um número entre 1 e 3 para a escolha")
                continue
            
class VerificaDados:

    def dados_d_usuario(self, conta_do_cliente):
        agencia = ""
        senha = 0
        tentativas = 0
        credenciais = False
        while True:
            while True:
                try:    
                    agencia = (input("Digite a agencia de cliente para verificação: "))
                    senha = int(input("Digite a senha de cliente para verificação: "))
                    break
                except ValueError:
                    print("Erro, digite digitos inteiros para a agencia e senha de usário")
            if agencia == conta_do_cliente.agencia and senha == conta_do_cliente.senha:
                print("Dados corretos, indo para a forma de pagamento\n")
                time.sleep(1)
                credenciais = True
                return credenciais
            
            
            if agencia != conta_do_cliente.agencia or senha != conta_do_cliente.senha:
                tentativas += 1
                print("Atenção, dados incorretos!!\n")
                if tentativas < 3:
                    print(f"Você tem {tentativas}/3 restantes\n")
                    time.sleep(1)
                else:
                    print("Número de tentativas excedido.. encerrando o programa\n")
                    time.sleep(1)
                    credenciais = False
                    return credenciais      


class Pagamentos:
    def __init__(self,numero,tipo):
        self.numero = numero
        self.tipo = tipo
    
    def PagamentoPix(self,conta_do_cliente):
        valtransf = 0
        cont = 0
        while True:
            try:
                print("Por favor, digite o valor a ser pago")
                valtransf = float(input("R$ "))
            except ValueError:
                print("Erro, valor digitado não compatível com o formato solicitado, porfavor, digite novamente... ")    
                continue
            if valtransf <= 0:
                print("O valor digitado não pode ser menor que zero, ou igual a zero,\n por favor digite o valor novamente...")
                time.sleep(1)
                continue
            
            if conta_do_cliente.saldo >= valtransf:
                conta_do_cliente.saldo -= (valtransf*0.90) # Desconto aplicado por ser em pix de 10%
                time.sleep(1)
                print(f"Transferência feita com sucesso!\n")
                time.sleep(1)
                break
            else:
                cont += 1
                print(f"Erro, valor solicitado é maior do que o saldo em conta, tente de novo\nSeu saldo atual em conta é de R${conta_do_cliente.saldo:.2f}")
            if cont == 3:
                print("número de tentativas excedido, saindo do modo de pagamento...")
                break
                
    def PagamentoCredito(self,conta_do_cliente):
        valcredito = 0
        cont = 0
        while True:
            
            try:
                print("Crédito escolhido, por favor digite o valor para passar no cartão..")
                
                valcredito = float((input("R$ ")).replace(",", "."))
            except ValueError:
                print("Erro, valor digitado não compatível com o formato solicitado, porfavor, digite novamente... ")    
                continue
            if valcredito <= 0:
                print("Erro, a compra não pode ser Zero, nem menor que zero...")
                time.sleep(1)
                continue
            
            if conta_do_cliente.limCartao >= conta_do_cliente.limiteusado + (valcredito + (valcredito*0.02)):
                conta_do_cliente.limiteusado =  conta_do_cliente.limiteusado + (valcredito + (valcredito * 0.02)) # 2% de juros em cima do valor em crédito
                time.sleep(1)
                print(f"Compra no crédito aprovada com sucesso!!\n")
                time.sleep(2)
                break
            else:
                cont += 1
                print(f"Erro, valor solicitado é maior do que o limite em conta, tente de novo..\n Seu limite atual é de R${(conta_do_cliente.limCartao-conta_do_cliente.limiteusado):.2f}\n")
            if cont == 3:
                print("número de tentativas excedido, saindo do modo de pagamento: Compra em crédito...")
                break
            
    def PagamentoDebito(self,conta_do_cliente):
        valdebito = 0
        cont = 0
        while True:
            
            try:
                print("Pagamento em débito escolhido, digite o valor a ser debitado.")
                valdebito = float(input("R$ "))
            except ValueError:
                print("Erro, valor digitado não compatível com o formato solicitado, porfavor, digite novamente... ")    
                continue
            if valdebito <= 0:
                print("O valor digitado não pode ser zero ou menor que zero\n Porfavor, tente de novo.")
                time.sleep(1)
                continue
            
            if conta_do_cliente.saldo >= valdebito:
                conta_do_cliente.saldo -= (valdebito-(valdebito*0.08))# Aplicado por compras no cartão de débito de 08% de desconto
                time.sleep(1)
                print(f"Compra no débito aprovada com sucesso!!\n")
                time.sleep(2)
                break
            else:
                cont += 1
                print(f"Erro, valor solicitado é maior do que o saldo em conta, tente de novo\n Seu limite atual é de R${(conta_do_cliente.saldo):.2f}")
            if cont == 3:
                print("número de tentativas excedido, saindo do modo de pagamento: Compra em débito...")
                break    

print("Bem-vindo ao banco A")
clienteA = ContaBanco() # Cria o objeto cliente
time.sleep(1)
print("Iniciando o sistema de cadastro..")
clienteA.Criausuario() #Chama o método do cliente
print("Gostaria de realizar algum pagamento?\n")
realizador_d_pag = ""

confirmando_dados = VerificaDados() # cria o objeto verificador de dados da conta do usuário.
Escpag = EscPagamento() # Cria objeto Escolha de pagamento, para o usuário.

while True:
    realizador_d_pag = input("[S] = Sim ou [N] = Não: ").strip().upper()
    if realizador_d_pag == "S":
        print("processando...")
        time.sleep(1)
        print("Iniciando o sistema...")
        time.sleep(1)
        credenciais = confirmando_dados.dados_d_usuario(clienteA) #Puxa o método de verificação credenciais do usuário.
        
        if credenciais:
            numero, tipo = Escpag.puxarpagamento()

            pag_em_pix = Pagamentos(numero,tipo)
            

            if numero == 1:
                pag_em_pix.PagamentoPix(clienteA)
            elif numero == 2:
                pag_em_pix.PagamentoCredito(clienteA)
            elif numero == 3:
                pag_em_pix.PagamentoDebito(clienteA)
                
            print(f"Escrevendo dados atuais da conta:\nNome:{clienteA.nome}\nSaldo da conta: {clienteA.saldo}\nLimite de atual do cartão: {(clienteA.limCartao-clienteA.limiteusado)}") 
                
        time.sleep(1)
        print("Gostaria de realizar outro pagamento?\n")
        time.sleep(1)
    elif realizador_d_pag == "N":
        print("Processando...")
        time.sleep(2)
        print(f"\nEscrevendo dados atuais da conta:\nNome:{clienteA.nome}\nSaldo da conta: {clienteA.saldo}\nLimite de cartão: {clienteA.limCartao}\n")    
        print("Encerrando o programa...")
        
        break
    else:
        print("Processando...")
        time.sleep(2)
        print("Erro, digite [S] para Sim ou [N] para não.\n")
    


