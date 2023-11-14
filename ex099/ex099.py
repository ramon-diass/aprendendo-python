from time import sleep


def maior(lst):
    sleep(2)
    print('Analisando os valores passados...')
    if len(lst) != 0:
        maior = lst[0]
        print(f'Foram informados {len(lst)} valores ao todo: ', end='')
        for n in lst:
            print(n, end=' ')
            sleep(.5)
            if n > maior:
                maior = n
        print(f'\nO maior valor informado foi o {maior}.')
        print('=' * 50)
    else:
        print('Não foi informado nenhum número.')
        print('O maior número foi 0')


l1 = [2, 5, 1, 7, 3, 4]
maior(l1)
l2 = [8, 3, 6]
maior(l2)
l3 = [1, 5, 9, 4, 0, 8, 15]
maior(l3)
l4 = []
maior(l4)
