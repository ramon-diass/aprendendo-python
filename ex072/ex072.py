print('\033[1;32mEscrevendo por extenso um número entre 0 e 20:\033[m')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('\nDigite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'O número digitado foi o {extenso[numero]}.')
        break
    print(f'O número {numero} não está entre 0 e 20!')
    continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        print('Não foi digitado nenhum número entre 0 e 20.')
        break
