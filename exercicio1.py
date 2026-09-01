# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#   Exiba:
#       Seu nome é {nome} ok
#       Seu nome invertido é {nome invertido} ok
#       Se nome contem {ou não} espaços
#       Seu nome tem n letras 
#       A Primeira letra do seu nome é {letra}
#       A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#   exiba "Desculpe, você deixou campos vazios"

nome = input('Usuário, digite seu nome: ')
idade = input('Usuário, digite sua idade: ')

if len(nome) > 0 and len(idade) > 0:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome tem espaço.')
    else:
        print(f'Seu nome não tem espaço.')
    print(f'Seu nome tem {len(nome)} caracteres.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')
else:
    print(f'Desculpe, você deixou campos vazios.')