print('-' * 60)
print('                   Loja Tem de Tudo')
print('-' * 60)
total = maior = quant = menor = 0
barato = ''
while True:
    produto = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço (R$): '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Adicionar mais produtos [S/N]? ').strip().upper()[0]
    total += preco
    quant += 1
    if preco > 1000:
        maior += 1
    if quant == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if continuar == 'N':
        break
print('-' * 23, end='')
print(' FIM ', end='')
print('-' * 32)
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {maior} produtos acima de R$1000.')
print(f'O produto mais barato foi {barato}, custando R${menor:.2f}.')
