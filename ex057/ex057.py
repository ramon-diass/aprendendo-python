print('\033[33mCadastro de sexo Masculino ou Feminino:\033[m\n')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('O valor digitado não é equivalente a Masculino ou Feminino. Digite o valor corretamente!')
print('\nSexo cadastrado com sucesso.')
