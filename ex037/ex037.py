from time import sleep

print('\033[1;35mCoversor de decimal para: binário, octal ou hexadecimal:\033[m\n')
print('''Escolha a base para a conversão: 
Digite [ 1 ] para binário
Digite [ 2 ] para octal ou 
Digite [ 3 ] para hexadecimal ''')
opcao = int(input('Opção: '))
num = int(input('Digite um número inteiro a ser convertido: '))
print('\n\033[1;33mFazendo a conversão...\033[m\n')
sleep(1.5)
if opcao == 1:
    print(f'O número {num} convertido para Binário é igual a {bin(num)[2:]}.')
elif opcao == 2:
    print(f'O número {num} convertido para Octal é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'O número {num} convertido para Hexadecimal é igual a {hex(num)[2:]}.')
else:
    print('Você não digitou a opção correta, tente novamente!')
