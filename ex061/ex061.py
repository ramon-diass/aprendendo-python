print('\033[4;32m        Gerador de PA:        \033[m\n')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o valor da razão: '))
pa = a1
c = 1
print(f'\n\033[33mOs 10 primeiros termos da PA são:\n{a1} ,', end='')
while c < 10:
    pa += r
    c += 1
    print(f' {pa} ', end='')
    print(',' if c < 10 else '.\033[m', end='')
