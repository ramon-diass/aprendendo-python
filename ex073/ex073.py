print('                      Colocação do brasileirão no dia 18/05/2023\n')
brasileirao = ('botafogo', 'palmeiras', 'fluminense', 'cruzeiro', 'athletico-PR', 'atletico-MG', 'santos', 'fortaleza', 'flamengo',
               'são paulo', 'grêmio', 'internacional', 'bragantino', 'bahia', 'goiás', 'vasco', 'corinthians', 'cuiabá',
               'coritiba', 'américa-MG')
print(f'Times do Campeonato Brasileiro 2023: {brasileirao}.')
print('-' * 100)
print(f'os 5 primeiros colocados: {brasileirao[:5]}.')
print('-' * 100)
print(f'Os quatros últimos colocados: {brasileirao[-4:]}.')
print('-' * 100)
print(f'Times em ordem alfabética: {sorted(brasileirao)}.')
print('-' * 100)
print(f'O time do Bahia está na {brasileirao.index("bahia") + 1}ª posição.')
