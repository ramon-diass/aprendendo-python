jogador = {'nome': input('Nome: ')}
soma = 0
quantGols = []
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(1, n+1):
    gol = int(input(f'Quantos gols na partida {g}? '))
    soma += gol
    quantGols.append(gol)
jogador['gols'] = quantGols
jogador['total'] = soma
print('==' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('==' * 20)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for c in range(0, n):
    print(f'     => Na partida {c+1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {soma} gols.')
