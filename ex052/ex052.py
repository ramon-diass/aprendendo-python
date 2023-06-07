print('\033[7;40m    Descubra se um número digitado é primo:     \033[m\n')
n = int(input('Digite um número inteiro para saber se ele é primo: '))
soma = 0
for div in range(n - 1, 1, -1):
    if n % div == 0:
        soma = soma + 1
if soma == 0:
    print(f'\033[36mO número {n} é um número primo.\033[m')
else:
    print(f'\033[31mO número {n} não é um número primo.\033[m')
