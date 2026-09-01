'''
Repetições
while (enquanto)
Executa uma ação enquanto ela for verdadeira
'''

condicao = True

while condicao:
    nome = input('Escreva um nome: ')
    print(f'O nome escrito foi {nome}.')

    if nome == 'sair':
        print('laço While foi interrompido com a palavra sair.')
        break



