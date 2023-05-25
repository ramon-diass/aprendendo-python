from random import choice
from time import sleep

print('Vamos jogar uma partida de \33[32mPedra\33[m, Papel ou \33[31mTesoura\33[m :)\n')
escolha = input('Escolha entre Pedra, Papel ou Tesoura: ').strip().title()
print('-' * 60)
lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
sleep(1)
print('\33[32mPedra\33[m')
sleep(1)
print('Papel')
sleep(1)
print('\33[31mTesoura\33[m')
print('-' * 60)
sleep(1)
if escolha == comp:
    print(f'\nAmbos escolhemos \33[34m{escolha}\33[m, empatamos!')
elif escolha == 'Pedra' and comp == 'Tesoura' or escolha == 'Papel' and comp == 'Pedra' or escolha == 'Tesoura' and comp == 'Papel':
    print(f'\nParabéns! Eu escolhi \33[34m{comp}\33[m. Você venceu!')
elif escolha == 'Tesoura' and comp == 'Pedra' or escolha == 'Pedra' and comp == 'Papel' or escolha == 'Papel' and comp == 'Tesoura':
    print(f'\nPerdeu! Eu escolhi \33[34m{comp}\33[m. Mais sorte para você da próxima vez!')
elif escolha != 'Pedra' and escolha != 'Papel' and escolha != 'Tesoura':
    print('Erro! Você não escoheu entre Pedra, Papel ou Tesoura!')
