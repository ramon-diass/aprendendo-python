print('Descobrir se esse ano é ano bissexto:')
print('--' * 20)
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano bissexto!')
else:
    print(f'O ano de {ano} não é um ano bissexto!')
