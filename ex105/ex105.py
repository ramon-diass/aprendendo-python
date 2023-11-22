def notas(*notas, sit=False):
    """
    Programa para adicionar n notas de um aluno, e avaliar sua situação.
    :param notas: recebe um número n de notas.
    :param sit: opcional, mostra se a situação do aluno é ruim, razoável ou boa, a depender da média.
    :return: retorna as informações do aluno.
    """
    aluno = {'Total': len(notas), 'Maior': max(notas), 'Menor': min(notas), 'Média': sum(notas)/len(notas)}
    if sit:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'Boa'
        elif aluno['Média'] >= 5:
            aluno['Situação'] = 'Razoável'
        else:
            aluno['Situação'] = 'Ruim'
    return aluno


resp = notas(5.5, 5, 7, 1, sit=True)
print(resp)
