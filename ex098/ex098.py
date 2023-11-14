from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ->', end=' ')
            cont += p
            sleep(.5)
        print('FIM')
        print('==' * 30)
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont} ->', end=' ')
            cont -= p
            sleep(.5)
        print('FIM')
        print('==' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora crie o seu próprio contador.')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
