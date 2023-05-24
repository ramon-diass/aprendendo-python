from datetime import date

print('\033[1;30;42m     CATEGORIA DE NATAÇÃO     \033[m\n')
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('')
if idade <= 9:
    print(f'Com a idade de {idade} anos, a categoria do atleta é MIRIM.')
elif idade <= 14:
    print(f'Com a idade de {idade} anos, a categoria do atleta é INFANTIL.')
elif idade <= 19:
    print(f'Com a idade de {idade} anos, a categoria do atleta é JUNIOR.')
elif idade <= 25:
    print(f'Com a idade de {idade} anos, a categoria do atleta é SÊNIOR.')
else:
    print(f'Com a idade de {idade} anos, a categoria do atleta é MASTER.')
