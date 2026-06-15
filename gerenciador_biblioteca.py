# Sistema de Gerenciamento de Biblioteca
# Funcionalidades:
# 1 - Cadastro os Usuários com validação de senha
# 2 - Login de Usuários
# 3 - Empréstimo de Livros com o controle de estoque

import time
from datetime import date
from datetime import datetime
import re

class Menu_de_acesso:
    def __init__(self):
        self.menu = 0
    
    def opcoes(self):
        while True:
            print("\nEscolha a sua ação em nosso sistema:\nPara loguin de usuários digite [1]\nPara cadastro de usuários digite [2]\nPara encerrar o programa [3]")
            try:
                self.menu = int(input("Digite a sua escolha: "))
                if self.menu == 1:
                    print("Acessando loguin de cliente..\n")
                    time.sleep(1)
                    return
                elif self.menu == 2:
                    return
                elif self.menu == 3:
                    print("Encerrando o programa...\n")
                else:
                    print("Erro, escolha uma opção entre as mostradas a cima...\n")
                    continue
                break
            except ValueError:
                print("Erro digite um valor inteiro, dentro, das opções para continuar")  

class Biblioteca:
    def __init__(self):
        self.__acessos_de_usuario = {}
        self.livros = {606025:["As cronicas de narnia Volume único",0, 5],706025:["Harry potter e a pedra filosofal", 0, 5],807025:["Senhor dos Aneis A sociedade do Anel", 0, 5],504025:["Jogos Vorazes", 0, 5],456525: ["Cosmos", 0, 5], 996535:["Uma breve história do tempo", 0, 5], 908025:["A arte da Guerra", 0, 5], 109025:["O principe de Maquiavel", 0, 5],204025:["O caso dos exploradores de caverna", 0, 5],896431:["A História do Universo para quem tem pressa", 0, 5]}
    def cadastro_d_clientes(self):
        nome = ""
        nome_d_acesso = ""

        #Cadastro de nome de usuário
        nome_repetido = True
        while nome_repetido:
            nome_repetido = True
            
            nome_d_acesso = (input("Digite o nome de acesso do usuário: ").replace(" ","").lower())
            if re.search(r'[^a-zA-Z0-9]',nome_d_acesso):
                print("Erro, o cadastro de acesso de usuário não pode conter caracteres especiais nem espaços")
                continue

            if nome_d_acesso in self.__acessos_de_usuario:
                print("Erro, o nome de acesso já existe, por favor digite um nome válido")
                continue
            print(f"nome do usuário: {nome_d_acesso} cadastrado!!\n")
            nome_repetido = False
            
        #Cadastro de nome de sistema.
        while True:
            # O sistema deve permitir que o nome de usuário contenha acentuação
            nome = (input("Digite o nome do que o usuário Gostaria de ser chamado: ").title().strip())
            if re.search(r'[^a-zA-ZÀ-ÿ ]',nome):
                print("Erro, o nome de usuário não pode ter caracteres especiais e números..\n Tente de novo..")
                continue
            break
        
        #Cadastro de senhas
        while True:
            print("\nCadastrando senha de usuário\n\nPor favor, siga as regras a seguir:\n1 - A senha no minimo oito digitos.\n2 - Deve ter pelo menos um caractere especial.\n3 - Deve ter uma letra maiuscula.\n")
            senha = input("Digite a senha: ")
            if len(senha) >= 8:
                if not re.search(r'[A-Z]',senha): 
                    print("Atenção, a senha precisa de pelo menos um caractere maiusculo..")
                elif not re.search(r'[^a-zA-Z0-9]', senha):
                    print("Atenção a senha precisa de pelomenos um caracatere especial")
                else:
                    print(f"Sucesso!! A senha: {senha} foi aceita, registrando...\n")  
                    break
            else:
                print("Atenção, o sistema não atende os requisitos mínimos de 8 caracteres\npor favor Tente novamente\n")
                continue
        
        novo_usuario = Usuario(nome_d_acesso, nome, senha)

        self.__acessos_de_usuario[nome_d_acesso] = novo_usuario 
        
    def login_de_cliente(self):
        acesso_usu_digitado = ""
        senha = ""
        
        if len(self.__acessos_de_usuario) == 0: 
            print("Erro, não temos usuários cadastrados em nosso sistema, voltando ao menu  ")
            return
        print("Por favor Digite seu nome de acesso\n")
        for erros in range (0,3):
            acesso_usu_digitado = input("usuário: ")
            senha = input("Senha: ")

            if acesso_usu_digitado in self.__acessos_de_usuario:
                cliente_encontrado = self.__acessos_de_usuario[acesso_usu_digitado]
                
                if cliente_encontrado.validar_senha(senha):
                    print("Sucesso, acesso concedido")
                    self.emprestimos(cliente_encontrado)
                else:
                    print("Erro, acesso ou senha inválidos, por favor, digite um acesso correto")
                    continue
                return
        print("Erro, acesso ou senha inválidos, por favor, digite um acesso correto\n")
    # Sistema de empréstimos de livros 
    def emprestimos(self,cliente_logado):
        while True:
            print(f"\n--- Atendimento: {cliente_logado.nome_de_usuario} ---")
            print("[1] Emprestar Livro")
            print("[2] Devolver Livro")
            print("[3] Voltar ao Menu Principal")
            
            selecao = input("--- Escolha ---")

            if selecao == "1":
                print("\n Livros Disponíveis ")
                
                tem_estoque = False
                for codigo, dados in self.livros.items():
                    nome_livro = dados[0]
                    qtd_alugada = dados[1]
                    qtd_total = dados[2]
                    
                    if qtd_alugada < qtd_total:
                        disponiveis = qtd_total - qtd_alugada
                        print(f"CÓDIGO: {codigo} | {nome_livro} ({disponiveis} disponíveis)")
                        tem_estoque = True
                
                if not tem_estoque:
                    print("Desculpe, nossa biblioteca está sem livros disponíveis no momento.")
                    continue
                
                while True:
                    try:
                        codigo_escolhido = int(input("\nDigite o CÓDIGO do livro que deseja alugar: "))
                        
                        if codigo_escolhido in self.livros:
                            if codigo_escolhido in cliente_logado.livros_emprestados:
                                print("Erro: O cliente já está com uma cópia deste livro!")
                                continue
                                
                            if self.livros[codigo_escolhido][1] < self.livros[codigo_escolhido][2]:
                                    while True:
                                        print('\n[Opções de Data]')
                                        data_input = input("Digite a data retroativa (DIA/MÊS/ANO) ou aperte ENTER para a data de hoje: ").strip()
                                        
                                        if data_input == "":
                                            data_de_emprestimo = date.today()
                                            break
                                        
                                        try:
                                            data_de_emprestimo = datetime.strptime(data_input, "%d/%m/%Y").date()
    
                                            if data_de_emprestimo > date.today():
                                                print("Erro, a informação não pode ser de uma data futura..")
                                                continue
                                            break
                                        except ValueError:
                                            print("Formato inválido: O usuário deve digitar da seguinte forma: DIA/MÊS/ANO")
                                                    
                                    self.livros[codigo_escolhido][1] += 1

                                    cliente_logado.guardar_livro_emprestado(codigo_escolhido, data_de_emprestimo)
                                

                                    print(f"Sucesso! O livro '{self.livros[codigo_escolhido][0]}' foi alugado com a data: {data_de_emprestimo.strftime('%d/%m/%Y')}.")
                                    break
                            else:
                                    print("Erro: Este livro específico está sem estoque em nosso acervo.")
                        else:
                            print("Erro, o Código do livro digitado não foi encontrato, tente de novo")
                        
                    except ValueError:
                        print("Erro: Digite um código numérico válido.")
                    
            elif selecao == "2":

                if not cliente_logado.livros_emprestados:
                    print("\nEste cliente não possui livros pendentes para devolução.")
                    continue
                
                print("\n--- Livros na Mochila do Cliente ---")
                for cod_livro, data_aluguel in cliente_logado.livros_emprestados.items():
                    nome_livro = self.livros[cod_livro][0]
                    print(f"CÓDIGO: {cod_livro} | {nome_livro} | Pego em: {data_aluguel.strftime('%d/%m/%Y')}")
                
                try:
                    codigo_devolver = int(input("\nDigite o CÓDIGO do livro para devolver: "))
                    
                    if codigo_devolver in cliente_logado.livros_emprestados:
                        data_que_pegou = cliente_logado.livros_emprestados[codigo_devolver]
                        dias_com_o_livro = (date.today() - data_que_pegou).days
                        
                        print(f"\nO cliente ficou com o livro por {dias_com_o_livro} dias.")
                        if dias_com_o_livro > 7:
                            dias_atraso = dias_com_o_livro - 7
                            valor_multa = dias_atraso * 2.00
                            print(f"ATENÇÃO: Livro devolvido com {dias_atraso} dias de atraso!")
                            print(f"Gerando multa no valor de: R$ {valor_multa:.2f}")
                        else:
                            print("Livro devolvido no prazo correto.")
                            
                        cliente_logado.devolver_livro_emprestado(codigo_devolver)
                        self.livros[codigo_devolver][1] -= 1
                        print("Devolução concluída com sucesso no sistema!")
                        
                    else:
                        print("Erro: O cliente não está com este livro.")
                except ValueError:
                    print("Erro: Digite um código numérico válido.")

            elif selecao == "3":
                print("Saindo do atendimento...")
                break
            
            else:
                print("Opção inválida.")
                
class Usuario:

    def __init__(self,nome_do_acesso, nome_usuario, senha): 
        self.nome_de_acesso = nome_do_acesso
        self.nome_de_usuario = nome_usuario
        self.livros_emprestados = {}
        self.__senha = senha
        
    def validar_senha(self, senha_informada):
        return self.__senha == senha_informada
    
    def guardar_livro_emprestado(self, codigo_do_livro, data_do_aluguel):
        self.livros_emprestados[codigo_do_livro] = data_do_aluguel
        
    def devolver_livro_emprestado(self, codigo_do_livro):
        del self.livros_emprestados[codigo_do_livro]    

print("\nBiblioteca Fictícia 01\nIniciando sistema")
    
Biblio1 = Biblioteca()
menu_principal = Menu_de_acesso()
while True:
    menu_principal.opcoes()
    if menu_principal.menu == 1:
        
        print("você entrou em atendimento do cliente\n")
        Biblio1.login_de_cliente()
    
    elif menu_principal.menu == 2:
        print("Acessando o sistema de cadastro de usuários...\n")
        laco = ""

        while True:
            Biblio1.cadastro_d_clientes()
            print("Gostaria de estar cadastrando um novo usuário? \n")
            laco = input("Escolha [S] para continuar e [N] para sair: ").strip().lower()
            if laco == "n":
                print("Encerrando cadastro de usuários..")
                break
            elif laco == "s":
                print("Continuando o programa..\n")
            else:
                print("Erro, a entrada deve ser 'S' para continuar e 'N' para encerrar o sistema de cadastros\nTente de novo...")
                continue
    elif menu_principal.menu == 3:
        print("Encerrando o programa")
        break
        
