cid = input('Digite o nome de uma cidade: ').strip
div = cid.split()
print(f'A cidade {cid} tem "Santo" no começo? {"SANTO" in div[0].upper()}')
