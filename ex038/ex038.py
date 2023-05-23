print('\033[7;34;40mComparador de dois números:\033[m\n')
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print(f'\nO \033[1;32mprimeiro número {n1}\033[m é maior do que o \033[33msegundo número {n2}\033[m.')
elif n2 > n1:
    print(f'\nO \033[1;32msegundo número {n2}\033[m é maior do que o \033[33mprimeiro número {n1}\033[m.')
else:
    print('\n\033[31mNão existe valor maior, ambos são iguais!\033[m')
