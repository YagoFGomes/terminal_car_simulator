def ligaCarro(carro_esta_ligado):
    liga = f"Carro ligando"
    carro_esta_ligado = True
    print(liga)
    return carro_esta_ligado
def DesligaCarro(carro_esta_ligado, velocidade_carro):
    if carro_esta_ligado and velocidade_carro == 0:
        desliga = f"Carro desligando"
    elif velocidade_carro >= 100:
        print('Você capotou o carro')
        exit()
    else: 
        desliga = "O carro não está ligado!"
    print(desliga)
  
"""
def VireEsquerda():
    vire = f"Virando a esquerda"
    print(vire)

def VireDireita():
    vire = f"Virando a direita"
    print(vire)
"""
def Vire(lado, velocidade_carro, carro_esta_ligado):
    if carro_esta_ligado and velocidade_carro > 0:
        if velocidade_carro > 30:
            print('Reduzindo velocidade para 30km/h')
            velocidade_carro = 30
        print(f'Virando para {lado}')
    else:
        print('O Carro está parado')    
    return velocidade_carro
        
        
    vire = f"Virando"
    print(vire)

def Acelera(velocidade_carro, carro_esta_ligado):
    
    if carro_esta_ligado:
        acelera = f"Acelerando"

        if velocidade_carro == 0:
            velocidade_carro += 10
        else:
            velocidade_carro += 15
        print(acelera)
        return velocidade_carro
    else: 
        desligado = "O carro não está ligado!"
        print(desligado)
        return 0

def Freia(carro_esta_ligado, velocidade_carro):
    if carro_esta_ligado and velocidade_carro > 0 :
        freio = f"Freiando"
        velocidade_carro = velocidade_carro - 10
        if velocidade_carro < 0:
            velocidade_carro = 0
    else:
        freio = f"Freiando, mas o carro está parado"
    print(freio)
    return velocidade_carro

def TomeiMulta(velocidade_carro):
    MULTA = 120
    if velocidade_carro > 120:
        print('Você levou uma multa leve')


