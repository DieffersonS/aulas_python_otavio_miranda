'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista

'''
import os
# --------- Variaveis ---------
opcao = ''
opcao_aceitavel = 'adls'
lista = []
nome_item = ''
valor_id = 0


# --------- Blocos ---------

while True:
    opcao = input('O que deseja fazer: \n[a] adicionar\n[d] deletar\n[l] listar\n[s] sair\nOpção: ' )

    if opcao not in opcao_aceitavel:
        print('A opção não está na lista.')
        continue
    
    if opcao in opcao_aceitavel:
        if opcao == 'a':
            nome_item = input('Qual item gostaria de adicionar à lista? \nItem: ')
            lista.append(nome_item)
            print(f'O item {nome_item} foi adicionado na lista.')

        elif opcao == 'd':
            valor_id = int(input('Qual o id do item que deseja deletar? \nId: '))
            
            for indice, item in enumerate(lista):
                if indice == valor_id:
                    del lista[indice]
                    print(f'O item {item} foi deletado da sua lista.')
  
        elif opcao == 'l':
            os.system('cls')
            print('Sua lista: ')
            for item in lista:                
                print('id', lista.index(item), '->', item )

        
        
    if opcao == 's':
        break
