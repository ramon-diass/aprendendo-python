print('--- Preço da passagem: ---')
dist = int(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    valor = dist * 0.5
    print(f'Para uma viagem de {dist} Km, o valor da passagem é de R${valor:.2f}.')
else:
    valor = dist * 0.45
    print(f'Para uma viagem de {dist} Km, o valor da passagem é de R${valor:.2f}.')
print('------ FIM ------')
