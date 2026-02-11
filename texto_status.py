import string
import unicodedata
# Projeto simples de verificador de elementos dentro de uma frase, Conta consoantes, vogais, e caracteres especiais.
# Retorna em porcentagem a quantidade de cada elemento.

class textoStatus:

    def __init__(self):
        self.texto = " "
        self.vogais = "AEIOU"
        self.Car_especiais = string.punctuation

    def remover_acentos(self, texto_bruto):
        transformador = " "
        texto_limpo = " "
        
        transformador = unicodedata.normalize('NFKD', texto_bruto)
        texto_limpo = "".join([c for c in transformador if not unicodedata.combining(c)])
        return texto_limpo.upper()


    def usu_entrada(self):
        print("=="*10,"Verificador básico de textos","=="*10)
        entrada_usuario = input("Digite um texto para ser analisado: ").strip()
        
        self.texto_original = entrada_usuario

        self.texto = self.remover_acentos(entrada_usuario)
        
    def contador(self):
        cont_vogais = 0
        cont_consoantes = 0
        cont_carEspeciais = 0
        caractere = 0
        informacoes = {1: 0, 2: 0, 3: 0}

        for caractere in self.texto:
            if caractere == "  ":
                continue


            if caractere in self.Car_especiais:
                cont_carEspeciais += 1

            elif caractere.isalpha():

                if caractere in self.vogais:
                    cont_vogais += 1
                else:
                    cont_consoantes += 1

        informacoes[1] = cont_consoantes
        informacoes[2] = cont_vogais
        informacoes[3] = cont_carEspeciais
        return informacoes

    def estatistica(self,diciona_estatistico):
        cont_final = 0
        percento_consoante = 0
        percento_vogal = 0
        percento_carEsp = 0
        cont_final = sum(diciona_estatistico.values())

        if cont_final == 0:
            print("Nenhum caractere válido encontrado para gerar a estatistica")
            return

        percento_consoante = (diciona_estatistico[1] /cont_final) *100
        percento_vogal = (diciona_estatistico[2] /cont_final) *100
        percento_carEsp = (diciona_estatistico[3] /cont_final) *100


        print("=="*10,"Informações de percentual","=="*10)
        print(f"\nA quantidade de caracretes registrada foi de: {cont_final}")
        print(f"\nO percentual de consoantes é de: {percento_consoante:.2f}%")
        print(f"\nO percentual de vogais é de: {percento_vogal:.2f}%")
        print(f"\nO percentual de caracteres especiais é de: {percento_carEsp:.2f}%\n")



analisar_texto = textoStatus()
analisar_texto.usu_entrada()
informacoes = analisar_texto.contador()
analisar_texto.estatistica(informacoes)