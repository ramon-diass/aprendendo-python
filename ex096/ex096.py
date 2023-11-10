def area(l, c):
    area = l * c
    print(f'A área de um terreno {larg:.2f}m x {comp:.2f}m é de {area:.2f} m².')


print(f'\033[1;32m{"Controle de Terreno":^50}\033[m')
print('=' * 50)
larg = float(input('Largura do terreno em metros: '))
comp = float(input('Comprimento do terreno em metros: '))
area(larg, comp)
