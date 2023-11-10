cadastro = list()
pessoa = dict()
mulher = []
acimaMedia = []
soma = 0
while True:
    pessoa.clear()
    pessoa = {'nome': input('Nome: ').strip().title(),
              'sexo': input('Sexo [M/F]: ').strip().title()[0],
              'idade': int(input('Idade: '))}
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if continuar == 'N':
        break
print('==' * 20)
print(f'- Foram cadastradas {len(cadastro)} pessoas.')
media = soma / len(cadastro)
print(f'- A média de idade foi de {media:.1f} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas com idade acima da média:')
for p in cadastro:
    if p['idade'] > media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}.', end=' ')
        print()
print(f'{"<< ENCERRADO >>":^40}')
