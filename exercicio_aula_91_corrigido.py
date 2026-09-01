'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
'''

import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar ou [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Item: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        
        except ValueError:
            print('Por favor, digite um número inteiro')
        
        except IndexError:
            print('Índice não existe na lista')
            
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Sua lista está vazia.')

        for i, valor in enumerate(lista):
            print(i, valor)
    
    elif opcao == 's':
        break

    else:
        os.system('cls')
        print('Escolha uma opção válida entre a, i ou l')
