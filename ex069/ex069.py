print('       Cadastro de Idade e Sexo:')
maior = homem = mulhermenor = 0
while True:
    print('-' * 40)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('\nQuer continuar [S/N]? ').strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    if continuar == 'N':
        break
print('-' * 40)
print(f'Dos cadastrados tivemos {maior} pessoas com 18 anos ou mais.')
print(f'Foram cadastrados {homem} homens.')
print(f'E tivemos {mulhermenor} mulheres com menos de 20 anos.')
