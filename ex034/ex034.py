print('--- Calculadora de Aumento Salarial ---')
sal = int(input('Digite o salário atual: R$'))
print('--' * 20)
if sal <= 1250:
    nsal = sal * 1.15
    print(f'Para um salário de R${sal:}, terá um aumento de 15% e seu novo valor será de R${nsal:.0f}.')
else:
    nsal = sal * 1.1
    print(f'Para um salário de R${sal:}, terá um aumento de 10% e seu novo valor será de R${nsal:.0f}.')
