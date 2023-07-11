print('\033[4;32m        Gerador de PA:        \033[m\n')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o valor da razão: '))
pa = a1
c = 1
print(f'\033[33mOs 10 primeiros termos da PA são:\n{a1} ,', end='')
while c < 10:
    pa += r
    c += 1
    print(f' {pa} ', end='')
    print(',' if c < 10 else '.\033[m', end='')
condicao = False
while not condicao:
    c2 = 0
    termos = int(input('\n\nVocê quer saber mais qunatos termos? '))
    c += termos
    if termos == 0:
        condicao = True
    elif termos < 0:
        print('Valores negativos não são permitidos!', end='')
    while c2 < termos:
        pa += r
        c2 += 1
        print(f'\033[1;33m{pa} ', end='')
        print(',' if c2 < termos else '.\033[m', end='')
print(f'\n\033[31mPrograma encerrado! Foram calculados {c} termos.\033[m')
