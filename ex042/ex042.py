print('\033[4;37mTriângulos\033[m\n')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print('')
if abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r1 - r2) < r3 < r1 + r2:
    print(f'\033[32mOs segmentos de reta {r1:.2f}, {r2:.2f} e {r3:.2f} podem formar um triângulo.\033[m')
    if r1 == r2 == r3:
        print('Como todos as retas são iguais, o triângulo é \033[36mEquilátero\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Como duas retas tem o mesmo tamanho, o triângulo é \033[36mIsósceles\033[m.')
    else:
        print('Como todas as retas são diferentes, o triângulo é \033[36mEscaleno\033[m.')
else:
    print(f'\033[31mOs segmentos de reta {r1:.2f}, {r2:.2f} e {r3:.2f} não podem formar um triângulo.\033[m')
