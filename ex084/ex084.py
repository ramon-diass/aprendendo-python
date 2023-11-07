dados = []
pessoas = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso em Kg: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Cadstrar mais pessoas [S/N]? ').strip().upper()[0]
    print('-' * 80)
    if continuar == 'N':
        break
print(f'Foram cadastrados {len(pessoas)} pessoas.')
maior = menor = pessoas[0][1]
for c in range(0, len(pessoas)):
    if pessoas[c][1] > maior:
        maior = pessoas[c][1]
    if pessoas[c][1] < menor:
        menor = pessoas[c][1]
print(f'O maior peso cadastrado foi de {maior}Kg, de:', end=' ')
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maior:
        print(f'[{pessoas[c][0]}]', end=' ')
print('.')
print(f'O menor peso cadastrado foi de {menor}Kg, de:', end=' ')
for c in range(0, len(pessoas)):
    if pessoas[c][1] == menor:
        print(f'[{pessoas[c][0]}]', end=' ')
print('.')
