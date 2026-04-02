import time
class validador:
    def __init__(self):
        self.senha = 0

    # uma letra maiuscula, um número, um caractere especial
    def entrada_senha (self):
        Caracteres_especiais = ["@", ".", "*", "'", '"', "+", "-", ':', ";", "$", "£", "&", "¢","#"]


        print('\n','=='*20,'Verificador de senhas', '=='*20)
        time.sleep(1)
        print('A senha deve ter:\n1° Oito digitos. \n2° Ter pelo menos uma letra Maiúscula.\n3° Ter um caractere especial.')
        time.sleep(1)
        while True:
            encontrar_maiusculo = False
            encontrar_numero = False
            encontrar_especial = False
            conta_tamanho = 0
            
            self.senha = input('\nDigite a senha: ')

            if len(self.senha) < 8:
                print("=="*2,"Erro, senha com quantidade menor de caracteres do que o permitido, digite novamente!!!", "=="*2)
                time.sleep(1)
                continue

            for contem in (self.senha):
                conta_tamanho += 1
                if contem.isupper():
                    encontrar_maiusculo = True
                if contem.isdigit():
                    encontrar_numero = True
                if contem in Caracteres_especiais:
                    encontrar_especial = True
            
            if encontrar_maiusculo == True and encontrar_numero == True and encontrar_especial == True:
                print("Entrada aceita!!\n")
                break
            else:
                print("Erro, a senha não atende os padrões solicitados..\n")
                time.sleep(2)
                continue
        print('Saindo do programa')









valida_Sn = validador()
valida_Sn.entrada_senha()



