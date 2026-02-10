import time

class temporizador:
    def __init__(self):

        self.minutos = 0
        
    def solicitar_tempo(self):
        while True:
            try:
                tempo = int(input("digite o tempo em minutos: "))
                self.minutos = tempo

                if self.minutos == 0:
                    print("Defina o tempo para iniciar!!")
                    return
                break
            except ValueError:
                print('Erro, digite o valor em formato inteiro \n')

    def iniciar (self):
        
        print(f"Iniciando a contagem número > {self.minutos} minutos...<")
        time.sleep(1)
        
        while self.minutos > 0:
            self.minutos -= 1
            for segundos in range (59, -1,-1):
                print(f'{self.minutos:02d}:{segundos:02d}', end= '\r') #o \n faz o código escrever o texto em cima do outro
                time.sleep(1)

meu_timer = temporizador()
meu_timer.solicitar_tempo()
meu_timer.iniciar()

print("fim do programa!!!")