print('\033[1;34m     Soma de n valores digitados por usuário:\033[m\n')
soma = cont = 0
while True:
    n = int(input('Digite um número ou 999 para encerrar: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\n\033[36mForam digitados {cont} números e a soma desses números foi {soma}.\033[m')
