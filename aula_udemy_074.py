'''
For + Range
range -> range(start, stop, step)

'''

# numeros = range(3, 31, 3)

# for numero in numeros:
#     print(numero)


# Exemplo da aula 76

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print ('For completo com sucesso!')