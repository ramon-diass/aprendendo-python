lista = (int(input('Digite o primeiro número: ')),
         int(input('Digite o segundo número: ')),
         int(input('Digite o terceiro número: ')),
         int(input('Digite o quarto número: ')))
print(f'\nForam digitados os seguintes números: {lista}.')
print(f'O número 9 apareceu {lista.count(9)} vez(es).')
if 3 in lista:
    print(f'O primeiro número 3 aparece no {lista.index(3) + 1}° número da lista.')
else:
    print('Não foi digitado nenhum número 3.')
print('Os valores pares digitados foram: ', end='')
par = 0
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
        par += 1
if par == 0:
    print('Nenhum número par')
