print('\033[4;40m          Tabuada:          \033[m\n')
n = int(input('Digite um número inteiro para saber sua tabuada: '))
for tab in range(1, 11):
    print(f'{n} x {c} = {n * tab}')
