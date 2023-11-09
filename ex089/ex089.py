ficha = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    continuar = input('Cadastrar mais alunos [S/N]? ').upper().strip()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'{"N°":<5}{"NOME":<10}{"MÉDIA:":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    nota = int(input('Mostrar nota de qual aluno (999 para interromper)? '))
    if nota == 999:
        print('Finalizando...')
        break
    if nota <= len(ficha) - 1:
        print(f'Notas de {ficha[nota][0]} são {ficha[nota][1]}')
