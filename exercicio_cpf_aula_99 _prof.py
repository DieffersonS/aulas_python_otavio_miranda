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

# variáveis
cpf = '11441490701'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

