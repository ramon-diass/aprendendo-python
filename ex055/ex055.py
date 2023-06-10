print('Leitor de maior e menor peso:\n')
maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input(f'Qual o peso da {cont}ª pessoa em Kg: '))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'\nO maior peso digitado foi: {maior}Kg.')
print(f'O menor peso digitado foi: {menor}Kg.')
