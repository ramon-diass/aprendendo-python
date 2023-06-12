from time import sleep

print('\033[7;40m     Programa com Menu:     \033[m\n')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
sair = False
while not sair:
    print('''
    MENU: Escolha uma opção
    [1] somar
    [2] multiplicar
    [3] saber o maior
    [4] novos números
    [5] sair do programa''')
    escolha = int(input('\033[1;33mDigite uma das opções acima:\033[m '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'O valor da multiplicação entre {n1} e {n2} é {mult}.')
    elif escolha == 3:
        if n2 > n1:
            print(f'O número {n2} é maior do que {n1}.')
        elif n1 == n2:
            print('Os dois números são iguais.')
        else:
            print(f'O número {n1} é maior do que {n2}.')
    elif escolha == 4:
        n1 = int(input('Escolha um novo primeiro número: '))
        n2 = int(input('Esvolha um novo segundo número: '))
    elif escolha == 5:
        sair = True
        print('Finalizando...')
    else:
        print('Opção Inválida. Selecione uma das opções abaixo!')
    sleep(3)
print('\n\033[31mPrograma encerrado!\033[m')
