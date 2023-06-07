soma = 0
for cont in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'\nA soma somente dos números pares que você digitou é: \033[31m{soma}\033[m')
