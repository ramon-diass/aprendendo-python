n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))
print('--' * 20)
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if n3 > maior:
    maior = n3

if n3 < menor:
    menor = n3

print(f'Dentre os números {n1}, {n2} e {n3}:\nO maior é {maior}.\nO menor é {menor}.')
