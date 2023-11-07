geral = [[], []]
for n in range(1, 8):
    numero = int(input(f'Digite o {n}° número: '))
    if numero % 2 == 0:
        geral[0].append(numero)
    else:
        geral[1].append(numero)
geral[0].sort()
geral[1].sort()
print('-' * 70)
print(f'Os valores pares digitados foram: {geral[0]}.')
print(f'Os valores ímpares digitados foram: {geral[1]}.')
