# Qual o menor número divisível por 1 a 20
# O menor número divisível por 1 a 10 é 2520

# Será que 2520 é a multiplicação dos números primos de 1 a 10?

def Multiplicacao1a10():
    MenorNumero = 1 * 2 * 3 * 5 * 7
    return MenorNumero

result = Multiplicacao1a10()
print(result)

# Resultado é 210, logo Não. E se decompormos os números de 1 a 10?
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 2 * 2
# 5 = 5
# 6 = 2 * 3
# 7 = 7
# 8 = 2 * 4 = 2 * 2 * 2
# 9 = 3 * 3 
# 10 = 5 * 2
# MenorNumero = 1*2*3*2*5*7*2*3

resultado = 1*2*3*2*5*7*2*3
print(resultado)

# Resultado é 2520. Logo, sim!

# 11 = 11
# 12 = 4 * 3 = 2 * 3 * 3
# 13 = 13
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 8 * 2 = 2 * 2 * 2 * 2
# 17 = 17
# 18 = 9 * 2 = 3 * 3 * 2
# 19 = 19
# 20 = 10 * 2 = 5 * 2 * 2
# MenorNumero = 1*2*3*2*5*7*2*3*11*13*2*17*19

resultado = 1*2*3*2*5*7*2*3*11*13*2*17*19
print(resultado)

# Para tornar o algoritmo realmente sofisticado e relevante precisamos decompor os números em primos e construir o número em cima deles
