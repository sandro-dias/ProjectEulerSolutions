# Qual o menor n�mero divis�vel por 1 a 20
# O menor n�mero divis�vel por 1 a 10 � 2520

# Ser� que 2520 � a multiplica��o dos n�meros primos de 1 a 10?

def Multiplicacao1a10():
    MenorNumero = 1 * 2 * 3 * 5 * 7
    return MenorNumero

result = Multiplicacao1a10()
print(result)

# Resultado � 210, logo N�o. E se decompormos os n�meros de 1 a 10?
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

# Resultado � 2520. Logo, sim!

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

# Para tornar o algoritmo realmente sofisticado e relevante precisamos decompor os n�meros em primos e construir o n�mero em cima deles
