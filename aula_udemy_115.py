def executar(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x * x

v = executar(quadrado, 8)

# print(v)

# Exemplos de aula sobre Closure

def criar_xingamento(xingamento):
    def xingar(nome):
        return f'{nome} {xingamento}'
    return xingar

mandar_a_merda = criar_xingamento('Vai a merda')
chamar_de_arrombado = criar_xingamento('Seu arrombado!')

print(mandar_a_merda('João'))
print(chamar_de_arrombado('Robson'))

# Mais um exemplo de Closure

def criar_multiplicador(numero):
    def multiplicar(valor):
        return numero * valor
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(300))
print(triplo(4652165))
    