lista = list()
for cont in range(1, 6):
    num = int(input('Digite um número: '))
    if cont == 1 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado na última posição da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos + 1} da lista.')
                break
            pos += 1
print('-' * 50)
print(f'Os 5 números digitados foram {lista}.')
