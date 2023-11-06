expressao = input('Digite uma expressão: ')
abertura = fechamento = 0
for letra in expressao:
    if letra == '(':
        abertura += 1
    elif letra == ')':
        fechamento += 1
if abertura == fechamento:
    print('\033[1;36mSua expressão é válida!\033[m')
else:
    print('\033[1;31mSua expressão não é válida!\033[m')
