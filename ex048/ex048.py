print('       \033[1;32mSoma de todos os número ímpares e múltiplos de 3 entre 1 e 500\033[m\n')
soma = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        soma += n
print(f'\033[36mA soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é:\033[m {soma}')
