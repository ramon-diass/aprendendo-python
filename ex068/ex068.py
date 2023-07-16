from random import randint
from time import sleep

print('\033[7;40m        Jogo Par ou Ímpar:        \033[m')
cont = 0
while True:
    print('-' * 40)
    escolha = input('Você escolhe Par ou Ímpar (P/I)? ').strip().upper()[0]
    jogador = int(input('Que número você escolhe? '))
    computador = randint(1, 10)
    print('')
    sleep(.8)
    print('1.. ', end='')
    sleep(.8)
    print('2.. ', end='')
    sleep(.8)
    print('3.. ', end='')
    sleep(.8)
    print('JÁ!')
    print('')
    sleep(.8)
    if escolha == 'P':
        if (jogador + computador) % 2 == 0:
            print(f'Você jogou {jogador} e eu escolhi {computador}, {jogador+computador} é PAR.')
            print('Você venceu! Vamos jogar novamente.')
        else:
            print(f'Você jogou {jogador} e eu escolhi {computador}, {jogador + computador} é ÍMPAR.')
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if (jogador + computador) % 2 != 0:
            print(f'Você jogou {jogador} e eu escolhi {computador}, {jogador + computador} é ÍMPAR.')
            print('Você venceu! Vamos jogar novamente.')
        else:
            print(f'Você jogou {jogador} e eu escolhi {computador}, {jogador + computador} é PAR.')
            print('Você perdeu!')
            break
    cont += 1
print('-' * 40)
print(f'FIM DE JOGO! Você venceu {cont} vezes.')
