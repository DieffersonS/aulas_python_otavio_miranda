primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("DIgite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor é maior, pois {primeiro_valor} é maior que {segundo_valor}.")
elif segundo_valor > primeiro_valor:
    print(f"O segundo valor é maior, pois {segundo_valor} é maior que {primeiro_valor}.")
else:
    print(f"Os valores são iguais!")

