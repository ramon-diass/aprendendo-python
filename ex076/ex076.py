print('Listagem com 1 tupla:')
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.35)
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
