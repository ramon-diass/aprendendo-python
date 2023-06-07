print('    \033[35mSoma dos 10 primeiros termos de uma PA:\033[m\n')
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = pt
soma = pt
for cont in range(1, 10):
    pa += r
    soma += pa
print(f'\nA soma dos 10 primeiros termos da PA com primeiro termo {pt} e razão {r} é \033[1;33m{soma}\033[m.')
