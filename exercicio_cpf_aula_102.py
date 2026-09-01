'''
Cálculo do SEGUNDO dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
Mais o PRIMEIRO DÍGITO,
Multiplicando cada um dos valores por uma
Contagem regressiva começando de 11

Ex: (746.824.890-70) -> 746824890
11x  10x  9x  8x  7x  6x  5x  4x  3x  2x
 7    4   6   8   2   4   8   9   0   7 <-- PRIMEIRO DÍGITO
77   40  54  64  14  24  40   36  0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 x 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado for maior que 9:
O resultado então será 0

Se o resultado for menor ou igual a 9
O segundo digito deste CPF será igual numero que resta da conta por 11

'''
# variáveis

cpf_usuario = '10857797778'
nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11

resultado_digito_2 = 0
for digitos in dez_digitos:
    resultado_digito_2 += int(digitos) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


# VALIDANDO O CPF

cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"
print(f"cpf_usuario {cpf_usuario}")
print(f"cpf_gerado_pelo_calculo {cpf_gerado_pelo_calculo}" )
if cpf_usuario == cpf_gerado_pelo_calculo:
    print(f"{cpf_usuario} é Válido")
else:
    print(f"CPF inválido")

