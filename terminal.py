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
        velocidade_carro = Freia(carro_esta_ligado, velocidade_carro)
    if retorno == 3: 
        velocidade_carro = Vire('direita', velocidade_carro, carro_esta_ligado)
    if retorno == 4: 
        velocidade_carro = Vire('esquerda', velocidade_carro, carro_esta_ligado)
    if retorno == 5:
        DesligaCarro(carro_esta_ligado, velocidade_carro)
    print(f'O carro está a: {velocidade_carro} Km/h')
    TomeiMulta(velocidade_carro)