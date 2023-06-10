print('\033[1;33m--------------- Palíndromo ---------------\033[m\n')
print('Palíndromo é uma frase ou palavra que se pode ler, indeferentemente, da esquerda para direita ou vice-versa.\n')
frase = str(input('Digite uma frase ou palavra: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!')
