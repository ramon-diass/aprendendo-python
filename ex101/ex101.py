def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos, não é permitido votar.')
    elif 16 <= idade < 18 or idade >= 60:
        print(f'Com {idade} anos, o voto é opcional.')
    elif 18 <= idade < 60:
        print(f'Com {idade} anos, o voto é obrigatório.')


nasc = int(input('Qual o ano de nascimento? '))
voto(nasc)
