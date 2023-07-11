print('Média, maior e menor de n valores digitados pelo usúario:')
soma = 0
cont = 0
stop = False
while not stop:
    n = int(input('\nDigite um número: '))
    parar = input('Deseja colocar mais algum número [S/N]? ').strip().upper()
    if parar[0] in 'SN':
        soma += n
        cont += 1
        if cont == 1:
            menor = maior = n
        else:
            if menor > n:
                menor = n
            elif maior < n:
                maior = n
        if parar[0] == 'N':
            stop = True
    else:
        print('Você não digitou S ou N. O número acima será desconsiderado. Tente novamente!')
print(f'\nVocê digitou {cont} números, e a média desses valores é {soma/cont:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
