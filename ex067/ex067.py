print('                            Tabuada versão 3.0:\n')
print('\033[1;31mDigite um número para saber sua tabuada ou digite um número negativo para encerrar.\033[m')
while True:
    print('-' * 20)
    n = int(input('Número: '))
    print('-' * 20)
    cont = 1
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
print('\033[33mPrograma encerrado! Volte sempre.\033[m')
