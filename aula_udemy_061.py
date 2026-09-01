'''
Repetições
while (enquanto)
Executa uma ação enquanto ela for verdadeira
Loop infinito -> quando uma condição no código não tem fim
'''

contador  = 0

while contador < 20:
    
    contador = contador +1
    
    if contador == 10:
        print('Isso não exibe o número 10')
        continue
    
    print(contador)    
    
    if contador == 18:
        break
print('Fim do contador!')



