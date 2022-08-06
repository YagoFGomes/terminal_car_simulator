def ligaCarro(carro_esta_ligado):
    liga = f"Carro ligando"
    carro_esta_ligado = True
    print(liga)
    return carro_esta_ligado
def DesligaCarro(carro_esta_ligado):
    if carro_esta_ligado:
        desliga = f"Carro desligando"
    else: 
        desliga = "O carro não está ligado!"
    print(desliga)
  
def VireEsquerda():
    vire = f"Virando a esquerda"
    print(vire)

def VireDireita():
    vire = f"Virando a direita"
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

def Freia():
    freio = f"Freiando"
    print(freio) 
