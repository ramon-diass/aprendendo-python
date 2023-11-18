def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


n = input('Nome do jogador: ').strip().title()
g = input(f'Quantos gols fez: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
