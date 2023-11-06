lista = list()
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Esse número já foi adicionado.')
    else:
        lista.append(num)
        print('Número adicionado.')
    continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
    print('-' * 50)
    if continuar == 'N':
        break
for itemLista in lista:
    if itemLista % 2 == 0:
        par.append(itemLista)
    else:
        impar.append(itemLista)
lista.sort()
par.sort()
impar.sort()
print(f'\033[4;33mLista com todos os números digitados\033[m: {lista}')
print(f'\033[4;32mLista somente com os números pares\033[m: {par}')
print(f'\033[4;36mLista somente com os números ímpares\033[m: {impar}')
