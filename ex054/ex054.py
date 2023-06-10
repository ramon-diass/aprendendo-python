from datetime import date

print('\033[4;37m        Contador de Maioridade         \033[m\n')
adulto = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        adulto += 1
print(f'\nDas 7 pessoas em questão: \033[32m{adulto} já são maior(es) de idade\033[m e \033[36m{menor} são menor(es) de idade\033[m.')
