from utils import *

terminal = """
    0 - Liga
    1 - Acelera
    2 - Freia
    3 - Vire a direita
    4 - Vire a esquerda
    5 - Desliga
"""
carro_esta_ligado = False
velocidade_carro = 0

while True: 
    print(terminal)
    retorno = int(input("Selecione uma opção: "))
    if retorno == 0: 
        carro_esta_ligado = ligaCarro(carro_esta_ligado)
    if retorno == 1: 
        velocidade_carro = Acelera(velocidade_carro, carro_esta_ligado)
    if retorno == 2: 
        Freia()
    if retorno == 3: 
        VireDireita()
    if retorno == 4: 
        VireEsquerda()
    if retorno == 5:
        DesligaCarro(carro_esta_ligado)
    print(f'O carro está a: {velocidade_carro} Km/h')