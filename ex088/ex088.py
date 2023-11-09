from time import sleep
from random import randint

print(f'{" Gerador de palpites da MEGA SENA ":-^50}')
palpites = []
quant = int(input('Quantos palpites deseja? '))
for p in range(0, quant):
    cont = 0
    while True:
        x = randint(1, 60)
        if x not in palpites:
            palpites.append(x)
            cont += 1
        if cont == 6:
            break
    palpites.sort()
    print(f'Jogo {p + 1}: {palpites}')
    palpites.clear()
    sleep(1)
print(f'{" Boa Sorte ":-^50}')
