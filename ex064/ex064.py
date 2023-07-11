print('      Somador de diversos números:\n')
soma = 0
cont = 0
stop = False
while not stop:
    n = int(input('Digite um número para somar ou "999" para encerrar: '))
    if n == 999:
        stop = True
    else:
        soma += n
        cont += 1
print(f'\nVocê digitou {cont} números e a soma desses números foi {soma}.')
