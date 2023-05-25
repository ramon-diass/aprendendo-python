print('-------\033[1;35m Preço do Produto \033[m-------\n')
valor = float(input('Digite o valor total a ser pago: R$ '))
print('''Digite a forma de pagamento: 
[ 1 ] para dinheiro 
[ 2 ] para 1x no cartão
[ 3 ] para 2x no cartão 
[ 4 ] para 3x no cartão: ''')
pag = int(input('Digite a opção escolhida pelo cliente: '))
print('')
if pag == 1:
    print(f'O valor total de R${valor:.2f} terá um desconto de 10% no pagamento à vista, seu novo valor será \033[1;32mR${valor * 0.9:.2f}\033[m.')
elif pag == 2:
    print(f'O valor total de R${valor:.2f} terá um desconto de 5% com pagamento no cartão à vista, seu novo valor será \033[1;32mR${valor * 0.95:.2f}\033[m.')
elif pag == 3:
    print(f'O valor total de R${valor:.2f} não sofrerá alteração com pagamento no cartão para 2x.')
elif pag == 4:
    print(f'O valor total de R${valor:.2f} terá um acréscimo de 20% com pagamento no cartão para 3x, seu novo valor será \033[1;31mR${valor * 1.2:.2f}\033[m.')
else:
    print('Comando digitado INVÁLIDO! Refaça a operação.')
