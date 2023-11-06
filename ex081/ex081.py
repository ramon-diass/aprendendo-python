lista = list()
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Esse número já foi adicionado! Não pode repetir.')
    else:
        lista.append(num)
        print('Número dicionado com sucesso!')
    continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
    print('-' * 50)
    if continuar == 'N':
        break
print(f'\033[1;35mForam adicionados {len(lista)} números a lista.\033[m')
lista.sort(reverse=True)
print(f'\033[1;32mOs número em ordem decrescente são: {lista}.\033[m')
if 5 in lista:
    print('\033[1;33mO número 5 foi digitado.\033[m')
else:
    print('\033[3;31mO número 5 não foi digitado.\033[m')
