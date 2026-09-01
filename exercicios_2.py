"""
1- Faça um programa que que peça ao usuário pra digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

2- Faça um programa que pergunte a hora ao usuário e, baseando-se na horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

3- Faça um programa que peça o primeiro nome do usuário. Se o nome tiver quatro letras ou
menos, escreva:"Seu nome é curto." Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"
e maior que 6 letras escreva "Seu nome é muito grande"
"""

# Exercício 1
numero = input('Escreva um número inteiro: ')

if '.' in numero:
    print(f'Seu babaca, {numero} não é número nº inteiro. Reinicie o programa e tente novamente')

elif numero:
    print(f'Porra, bixo, texto não...')
    
else:
    novo_numero = int(numero)
    if novo_numero%2 == 0:
        print(f'O número {novo_numero} é PAR.')
    else:
        print(f'O número {novo_numero} é IMPAR')
    print(f'Segue o jogo...')

# Exercício 2

# hora = input('Que horas são? (Responda no formato "HH:MM"): ')

# if len(hora) < 5:
#     print(f'Coloque a hora no formato correto -> "HH:MM"')
# else:
#     hora_certa = int(hora[0:2])

# if hora_certa >= 0 and hora_certa <= 4:
#     print(f'São no momento {hora}h então, BOA MADRUGADA!')
# elif hora_certa >= 5 and hora_certa <= 11:
#     print(f'São no momento {hora}h então, BOM DIA!')
# elif hora_certa >= 12 and hora_certa <= 17:
#     print(f'São no momento {hora}h então, BOA TARDE')
# elif hora_certa >= 18:
#     print(f'São no momento {hora}h então, BOA NOITE')

# Exercício 3

# nome = input('Digite seu nome: ')

# qtd_carac = len(nome)

# if qtd_carac <= 4:
#     print(f'Seu nome é muito curto')
# elif qtd_carac >= 5 and qtd_carac <= 6:
#     print(f'Seu nome é normal')
# else:
#     print(f'Seu nome é muito longo')
    
