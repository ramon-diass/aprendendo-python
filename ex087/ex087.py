matriz = [[], [], []]
somapar = soma3col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor [{l}, {c}] da matriz: ')))
print('-' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3col += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-' * 50)
print(f'Soma de todos os valores pares da matriz: {somapar}')
print(f'Soma dos valores da terceira coluna: {soma3col}')
print(f'Maior valor da segunda linha: {maior}')
