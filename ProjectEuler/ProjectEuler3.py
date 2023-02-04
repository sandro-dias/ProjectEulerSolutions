#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?
 
def MaiorFatorPrimo(Number):
    Iterador = 2
    Fatores = []
    while Iterador * Iterador <= Number:
        if Number % Iterador:
            Iterador += 1
        else:
            Number //= Iterador
            Fatores.append(Iterador)
    if Number > 1:
        Fatores.append(Number)
    print(Fatores)
    return Number

MaiorFatorPrimo(600851475143)