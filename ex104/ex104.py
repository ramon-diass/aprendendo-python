def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            num = int(n)
            break
        else:
            print('\033[31mErro! Digite um número válido.\033[m')
    return num


n = leiaInt('Digite um número: ')
print(f'\033[36mVocê acabou de digitar o número {n}.\033[m')
