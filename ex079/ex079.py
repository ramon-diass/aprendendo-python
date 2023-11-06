lista = []
cont = 0
while True:
    print('-' * 46)
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Esse número já foi adicionado. Não pode duplicar!')
    else:
        lista.append(numero)
        cont += 1
        print('Número adicionado com sucesso!')
    resposta = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if resposta == 'N':
        break
print('-' * 46)
print(f'Foram digitados {cont} números válidos.')
lista.sort()
print(f'Esses números foram {lista}.')
