cadastro = list()
jogador = dict()
quantGols = list()
while True:
    jogador.clear()
    quantGols.clear()
    jogador = {'nome': input('Nome: ').title().strip()}
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(1, n+1):
        gol = int(input(f'Quantos gols na partida {g}? '))
        quantGols.append(gol)
    jogador['gols'] = quantGols[:]
    jogador['total'] = sum(quantGols)
    cadastro.append(jogador.copy())
    continuar = input('Deseja adicionar mais jogadores [S/N]? ').strip().upper()[0]
    while True:
        if continuar in 'NS':
            break
        print('Erro! Digite S ou N para continuar ou parar.')
    if continuar == 'N':
        break
print('==' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('==' * 20)
for k, v in enumerate(cadastro):
    print(f'{k+1:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar o levantamento de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    elif busca > len(cadastro):
        print(f'ERRO! Não existe um código para o número {busca}.')
    else:
        print(f'-- Levantamento do Jogador: {cadastro[busca-1]["nome"]} --')
        for i, g in enumerate(cadastro[busca-1]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('==' * 20)
print(f'{"<< ENCERRADO >>":^40}')
