# criar uma lista para pegar a soma dos multiplos de 3
# criar uma lista para pegar a soma dos multiplos de 5
# criar uma lista para pegar a soma dos multiplos de 15
# somar as duas primeiras e subtrair da terceira

def MultiplosAbaixoDe1000(numero):
    multiplicador = 1000/numero
    iterador = 1
    soma = 0
    while (iterador < multiplicador):
        soma = soma + numero*iterador
        iterador = iterador + 1
    return soma

resultado = MultiplosAbaixoDe1000(3) + MultiplosAbaixoDe1000(5) - MultiplosAbaixoDe1000(15)
print(resultado)