print('\033[1;33mBoletim Escolar\033[m\n')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('')
if media < 5:
    print(f'Com as notas {n1:.2f} e {n2:.2f}, a média do aluno foi {media:.2f} e com isso ele está \033[1;31mREPROVADO.\033[m.')
elif 5 <= media < 7:
    print(f'Com as notas {n1:.2f} e {n2:.2f}, a média do aluno foi {media:.2f} e com isso ele está em \033[1;30mRECUPERAÇÃO\033[m.')
else:
    print(f'Com as notas {n1:.2f} e {n2:.2f}, a média do aluno foi {media:.2f} e com isso ele está \033[1;36mAPROVADO\033[m.')
