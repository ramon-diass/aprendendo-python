print('Verificando se três segmentos de reta pode formar um triângulo:\n')
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
print('--' * 20)
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('As retas acima podem formar um triângulo!')
else:
     print('As retas acima não podem formar um triângulo!')
