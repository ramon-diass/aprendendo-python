from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando 5 valores: ', end='')
    for n in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[n], end=' ')
        sleep(.5)
    print()


def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num}, temos {soma}.')


numeros = []
sorteio(numeros)
somaPar(numeros)
