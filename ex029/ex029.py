veloc = int(input('Digite a velocidade do carro: '))
print('--' * 20)
if veloc <= 80:
    print(f'A velocidade do carro foi de {veloc} Km/h.')
    print('Tudo certo, o limite de velocidade não foi excedido!')
else:
    print(f'A velocidade do carro foi de {veloc} Km/h.')
    multa = (veloc - 80) * 7
    print(f'Por excesso de velocidade, uma multa foi gerada no valor de R${multa:.2f}.')
