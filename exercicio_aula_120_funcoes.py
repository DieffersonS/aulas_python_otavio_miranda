""""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""
def criar_multiplicador(numero):
    def multiplicador(valor):
        return numero * valor
    return multiplicador

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quadruplo = criar_multiplicador(4)

print(f'O dobro do valor é:', dobro(4))
print(f'O triplo do valor é:', triplo(8))
print(f'O quadruplo do valor é:', quadruplo(90))