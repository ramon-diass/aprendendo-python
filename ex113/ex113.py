def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except ValueError:
            print('\033[31mDigite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar um número inteiro.\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except ValueError:
            print('\033[31mDigite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar um número inteiro.\033[m')
            return 0
        else:
            return real


i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o valor real digitado foi {f}.')
