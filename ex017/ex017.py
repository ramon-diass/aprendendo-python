from math import hypot, sqrt

adj = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do cateto oposto: '))
hip = sqrt(adj**2 + op**2)
print(f'Através da fórmula de cálculo da hipotenusa, ela é igual a {hip:.2f}')
print(f'Usando a import, sua hipotenusa é: {hypot(adj, op):.2f}')
