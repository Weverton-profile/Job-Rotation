from math import sqrt

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonacci(busca):
    array = []
    n = 0
    atual = F(n)
    while int(atual) <= busca:
        if 0 <= atual:
            array.append(int(atual))
        n += 1
        atual = F(n)
    resultado(busca, array)

def resultado(busca, array):
    for i in range(len(array)):
      print(f'{array[i]} ', end="")
    print(".")
    if busca in array:
      print(f'O numero {busca} pertence a sequencia.')
    else:
      print(f'O numero {busca} não pertence a sequencia.')

Fibonacci(100)