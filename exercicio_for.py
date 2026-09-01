'''
Faça um jogo para o usuário adivinhar qual a plavara secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a eltra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exibe a letra;
- Se a letra digitada estiver errada, exiba *.
Faça a contagem de tentativas do seu usuário.
'''

# Jogo adivinhe a palavra.

import os

# - - - - - Variáveis

palavra_secreta = 'hipotermia' # Variavel da palavra secreta
letra = '' # Variável que pega a letra digitada a ser usada
letras_acertadas = '' # Variável que armazena as letras corretas chutadas
palavra_escondida = '' # Variável que mostra a palavra com as letras descobertas
contador = 0 # Variável que conta as tentativas d eacertar as letras

# - - - - - Laço de repetição para o programa executar até que seja interrompido.

while True:
    

    # Aqui a variavel recebe o input digitado
    letra = input('Digite a letra da palavra secreta: ')
    palavra_escondida = ''
    contador += 1

    
    # Este bloco verifica se foi digitado mais de uma letra.
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
        
    # Este bloco verifica se a letra digitada está na palavra secreta
    if letra in palavra_secreta:
        print('Acertou uma letra!')
        #print('Tentativas: ', contador)
    
    # Este bloco verifica se a letra não está na palavra secreta.
    else:
        print('Errou! Tente de novo!')
        #print('Tentativas: ', contador)

    # Este bloco preenche a palavra escondida, antes com "_" com os as letras acertadas
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    #print('As letras certas são: ', letras_acertadas)

    # Este bloco adiciona as letras 
    for letra_chutada in palavra_secreta:
        if letra_chutada in letras_acertadas:
            #print(letra_chutada)
            palavra_escondida += letra_chutada
        else:
            palavra_escondida += '_'
    print('Acertos: ', palavra_escondida)

    if '_' not in palavra_escondida:
        print('Parabéns! Você acertou a Palavra SECRETA!!!!')
        print(f'Você acertou em {contador} tentativas!')
        break


