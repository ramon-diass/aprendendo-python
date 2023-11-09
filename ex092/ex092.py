from datetime import date

pessoa = {'Nome': input('Nome: '), 'Idade': date.today().year - int(input('Ano de nascimento: ')),
          'CTPS': int(input('N° da Carteira de Trabalho (0 não tem): '))}
if pessoa['CTPS'] == 0:
    print('==' * 20)
    for k, v in pessoa.items():
        print(f'{k} tem valor {v}.')
else:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + 35
    print('==' * 20)
    for k, v in pessoa.items():
        print(f'{k} tem valor {v}.')
print(f'{" FIM ":=^40}')
