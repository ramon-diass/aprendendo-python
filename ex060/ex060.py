from math import factorial

print('\033[1;35mCalculadora de fatoriais:\033[m\n')
n = int(input('Digite um número: '))
cont = 0
print('')
print(f'{n}! = ', end='')
while cont < n:
    if cont < n - 1:
        print(f'{n - cont} x ', end='')
        cont += 1
    else:
        print(f'{n - cont} = {factorial(n)}.', end='')
        cont += 1
