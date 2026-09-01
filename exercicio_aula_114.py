"""
Exercicio com funções

Crie uma função que multiplique todos os argumentos
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variável

Crie uma funçao fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    

print(multi(1,2,3,5,5))


def verifica(x):
    if x%2 == 0:
        return print(f"O valor {x} é par")
    return print(f"O valor {x} é ímpar")

# verifica(60)