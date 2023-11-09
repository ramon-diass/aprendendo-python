aluno = {'Nome': input('Nome do aluno: '), 'Média': float(input('Média do aluno: '))}
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
if aluno['Média'] >= 6:
    print('Situação é igual a \033[1;36mAPROVADO\033[m.')
else:
    print('Situação é igual a \033[31mREPROVADO\033[m.')
