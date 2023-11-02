from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
maior = menor = numeros[0]
for lista in numeros:
    print(lista, end=' ')
print(f'\nO menor número sorteado foi: {min(numeros)}.')
print(f'O maior número sorteado foi: {max(numeros)}.')
