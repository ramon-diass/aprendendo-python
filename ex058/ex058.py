from random import randint

print('\033[4;34m        Jogo da Advinhação:        \033[m')
acertou = False
com = randint(0, 10)
cont = 0
while not acertou:
    jog = int(input('\nEm que número entre 0 e 10 eu estou pensando? '))
    cont += 1
    if jog < com:
        print('Mais! Tente outra vez...')
    elif jog > com:
        print('Menos! Tente outra vez...')
    else:
        acertou = True
print(f'\n\033[1;36mParabéns! Você conseguiu advinhar que o número que eu escolhi foi o {com}. Foram necessárias {cont} tentativas.\033[m')
