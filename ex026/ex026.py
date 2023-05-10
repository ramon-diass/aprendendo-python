frase = input('Digite uma frase: ').strip()
print(f'Quantas vezes apareceu a letra "a": {frase.lower().count("a")}')
print(f'A letra "a" aparece pela primeira vez na posição: {frase.lower().find("a") + 1}')
print(f'A letra "a" aparece pela última vez na posição: {frase.lower().rfind("a") + 1}')
