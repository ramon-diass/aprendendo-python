print('\033[7;40m     Caixa Eletrônico:     \033[m\n')
saque = int(input('Qual o valor do saque? R$ '))
nota50 = saque // 50
resto = saque % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota1 = resto // 1
if nota50 != 0:
    print(f'Será sacado {nota50} cédulas de R$50,00.')
if nota20 != 0:
    print(f'Será sacado {nota20} cédulas de R$20,00.')
if nota10 != 0:
    print(f'Será sacado {nota10} cédulas de R$10,00.')
if nota1 != 0:
    print(f'Será sacado {nota1} cédulas de R$1,00.')
