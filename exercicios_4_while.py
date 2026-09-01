nome = 'Joaquim José da Silva Xavier'

qtd_letras = len(nome)

contador = 0

novo_nome = '*'
while contador < qtd_letras:
    letra = nome[contador]
    contador += 1
    novo_nome += letra + '*'

print(novo_nome)