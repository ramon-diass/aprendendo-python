print('-' * 46)
print(f'{"Digite 5 números:":^46}')
print('-' * 46)
lista = list()
for cont in range(0, 5):
    lista.append(int(input('Digite um número: ')))
menor = maior = lista[0]
posmenor = posmaior = 0
for c, v in enumerate(lista):
    if v < menor:
        menor = v
        posmenor = c
    elif v > maior:
        maior = v
        posmaior = c
print('-' * 46)
print(f'Os 5 números digitados foram {lista}.')
print(f'O menor número foi o {menor} e aparece na posição {posmenor + 1}.')
print(f'O maior número foi o {maior} e aparece na posição {posmaior + 1}.')
