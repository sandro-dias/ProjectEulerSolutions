# iterar a série de Fibonacci até 4 milhões
# criar uma lista dos itens não-pares
# soma a lista

def CalculaOResto(numero):
    if (numero % 2 == 0):
        return True
    else: 
        return False

def SerieDeFibonacci():
    primeiroValor = 1
    segundoValor = 2
    somaDosImpares = 0
    while (segundoValor < 4000000):
        if(CalculaOResto(segundoValor)):
            somaDosImpares = somaDosImpares + segundoValor
        segundoValor = segundoValor + primeiroValor
        primeiroValor = segundoValor - primeiroValor
    return somaDosImpares

print(SerieDeFibonacci())
