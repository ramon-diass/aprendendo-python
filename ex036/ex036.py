from time import sleep

print('\033[1;32mAprovação de Empréstimo Bancário\033[m\n')
valor = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
ano = int(input('Em quantos anos você pretende pagar? ')) * 12
prestacao = valor / ano
sleep(.5)
print('\nCalculando, espere um momento...\n')
sleep(2)
if prestacao <= salario * 0.3:
    print(f'\033[1;36mParabéns! O empréstimo foi aprovado. O valor de R${valor:.2f} será pago em {ano} meses com prestação '
          f'fixada no valor de R${prestacao:.2f} por mês.\033[m')
else:
    print('\033[1;31mInfelizmente seu empréstimo foi negado.\033[m')
