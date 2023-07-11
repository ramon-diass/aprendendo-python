print('           \033[4;30;43m   Sequência de Fibonacci   \033[m')
termos = int(input('\nQuantos termos da sequência de Fibonacci você quer ver? '))
n1 = 0
n2 = 1
cont = 3
print('0 , 1', end='')
while cont <= termos:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    cont += 1
    print(f' , {fib}', end='')
print(f' .\n\n\033[32mEstes são os {termos} primeiros termos da sequência de Fibonacci!\033[m')
