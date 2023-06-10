print('\033[7;40m      Analisador Completo:      \033[m\n')
media = 0
velho = 0
cont = 0
velho = 0
pvelho = ''
for pessoa in range(1, 5):
    print(f'---- {pessoa}ª Pessoa: ----')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    media += idade
    if idade > velho and sexo == 'M':
        velho = idade
        pvelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f'\n\033[1;33mA média de idade do grupo é {media/4:.1f} anos.\033[m')
if velho != 0:
    print(f'\033[36m{pvelho} é o homem mais velho do grupo, com {velho} anos.\033[m')
else:
    print('\033[36mNo grupo não foi digitado as informações de nenhum homem.\033[m')
if cont != 0:
    print(f'\033[35mNo grupo tem {cont} mulher(es) com menos de 20 anos.\033[m')
else:
    print('\033[35mNo grupo não tem nenhuma mulher com menos de 20 anos.\033[m')
