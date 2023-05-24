from time import sleep

print('\033[7;40m          Cálculo de IMC:           \033[m\n')
peso = float(input('Digite o seu peso em Kg: '))
alt = float(input('Digite sua altura em metros: '))
print('')
imc = peso / alt ** 2
print('Calculando seu IMC...')
sleep(1.5)
if imc < 18.5:
    print(f'Sei IMC é {imc:.2f}, logo você está \033[4;36mAbaixo do Peso\033[m.')
elif 18.5 <= imc < 25:
    print(f'Sei IMC é {imc:.2f}, logo você está com o \033[4;32mPeso Ideal\033[m.')
elif 25 <= imc < 30:
    print(f'Sei IMC é {imc:.2f}, logo você está com \033[4;33mSobrepeso\033[m.')
elif 30 <= imc < 40:
    print(f'Sei IMC é {imc:.2f}, logo você está com \033[4;34mObesidade\033[m.')
else:
    print(f'Sei IMC é {imc:.2f}, logo você está com \033[4;31mObesidade Mórbida\033[m.')
