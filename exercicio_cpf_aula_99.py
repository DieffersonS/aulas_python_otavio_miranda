'''
Cálculo do PRIMEIRO dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
Multiplicando cada um dos valores por uma
Contagem regressiva começando de 10

Ex: (746.824.890-70) -> 746824890
10x  9x  8x  7x  6x  5x  4x  3x  2x
 7   4   6   8   2   4   8   9   0
70   36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 x 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado for maior que 9:
O resultado então será 0
O primeiro digito deste CPF é 7
'''
cpf = ''

while True:

    cpf = input('Digite o cpf sem pontos e traços:\n')
    valores = 0
    multiplicador = 10
    digito_verificador = '0'

    # Verifica se o cpf está com a quantidade de caracteres correto.
    if len(cpf) != 11:
        print(f'A quantidade de caracteres está incorreta.')
        continue
    
    for numeros in cpf:
        numeros = int(numeros)
        print(f'{numeros} x {multiplicador} = ',numeros * multiplicador )
        resultado_parcial = numeros*multiplicador
        valores = resultado_parcial+valores
        multiplicador -= 1
        if multiplicador == 1:
            break

    print(f'valores -> {valores}')

    valores_por_dez = valores*10

    print(f'valores x10 -> {valores_por_dez}')

    resto = valores_por_dez % 11

    print (f'Resto da divisão por 11 -> {resto}')

    if resto < 9:
        digito_verificador = str(resto)
        print(f'O décimo primeiro dígito é {resto}')
    else:
        print(f'O primeiro dígito do cpf é 0')
    
    if cpf[9] == digito_verificador:
        print(f'O cpf está ok')
    else:
        print(f'O cpf é inválido')
    deseja_sair = input('Deseja Sair?\nSim [s]\nNão [n]\n')

    if deseja_sair == 's':
        break
    else:
        continue