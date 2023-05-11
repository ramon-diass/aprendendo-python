from random import randint
from time import sleep

print('-' * 40)
print('Tente advinhar que número estou pensando.')
com = randint(0, 5)
usu = int(input('Qual será o número entre 0 e 5 que o computador escolheu? '))
print('-' * 40)
print('Carregando...')
sleep(3)
if com == usu:
    print(f'Parabéns! Você acertou. O número escolhido pelo computador foi {com}.')
else:
    print(f'Não foi dessa vez, tente novamente! O número escolhido pelo computador foi {com}.')
