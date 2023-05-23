from datetime import date

print('\033[31mAlistamento Militar:\033[m\n')
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f'\nAinda não chegou a sua vez. Faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print(f'\nVocê completou ou vai completar {idade} este ano. Está na hora de se alistar!')
else:
    print(f'\nVocê deveria ter se alistado há {idade - 18} anos atrás.')
