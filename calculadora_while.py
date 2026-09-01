'''
Calculadora com While
'''

# Entrando em um laço de repetição para executar de forma
# ininterrupta o programa (até que você queira sair)

while True:
    # Declarando as varáveis
    valor_1 = input('Digite um número: ')
    valor_2 = input('Digite um outro numero: ')
    operador = input('Digite o operador entre [+ - * /]: ')

    # Criando uma variável (Flag) para verificar se os níumeros são válidos
    numeros_validos = None

    # Declarando as varáveis fora do bloco para ter acesso fora dele
    numero_1_float = 0
    numero_2_float = 0

    # Abrindo um try para tratar exceções e o programa não quebrar
    try:
        # Transformando as variáveis de string parrra float
        numero_1_float = float(valor_1)
        numero_2_float = float(valor_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_ok = '+-*/'

    if operador not in operadores_ok:
        print ('O operador escolhodo é inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('O resultado da sua conta está abaixo:')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    else:
        print('Isso não deveria ser exibido. A não ser que haja um erro.')

    nome = input('Gostaria de sair? Aperte s para [s]im: ').lower().startswith('s')

    if nome is True:
        break