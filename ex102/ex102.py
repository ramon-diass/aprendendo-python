def fatorial(n):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado o fatorial.
    :return: O valor do fatorial de n.
    """
    print(f'{n} x ', end='')
    fat = n
    n -= 1
    while n > 0:
        print(n, end='')
        fat *= n
        n -= 1
        if n > 0:
            print(' x ', end='')
        else:
            print(' = ', end='')
    return fat


help(fatorial)
print(fatorial(5))
