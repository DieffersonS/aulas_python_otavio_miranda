"""
Escopo de Função em Python
Escopo significa o local onde aquele código pode atingir.
Existe o Escopo local e o global
O escopo Global, é o escopo que todo o código é alcançável
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

"""

x = 1

def escopo_1():
    x = 10
    print(x)
    def escopo_2():
        y = 5
        print(x,y)
    escopo_2()
x = 15

escopo_1()

"""
Retorno de Valores de funções (return)

"""

def soma():
    somatorio = 20 + 40
    return somatorio
   
print(soma())

"""
args - Argumentos não nomeados
* - *args (empacotamento desempacotamento)
"""

# lembrete de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def exemplo_args(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# somatorio = exemplo_args(1,2,3,4,5)
# print(f"a variavel somatorio é: ", somatorio)

numeros = (1,2,3,4,5,6,7,8,9)

print(numeros)
print(*numeros)