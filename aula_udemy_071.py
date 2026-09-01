frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a suscipit ligula, et imperdiet sem. Morbi aliquet tellus eu tortor volutpat, vel tincidunt felis posuere. Nullam sit amet sapien lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lacus mi, vulputate eget quam sit amet, vehicula congue tellus. Pellentesque ultrices posuere tellus, non iaculis orci finibus nec. Nulla ac sodales neque, quis vulputate lacus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In in commodo ex. Nunc sit amet posuere metus. Nulla et erat turpis. Nullam ac pellentesque neque. Etiam at dapibus diam.fferson'

i = 0

qtd_letra = 0
qtd_letra_atual = 0

while i < len(frase):
    letra = frase[i]
    if letra == ' ':
        i += 1
        continue
    
    qtd_letra = frase.count(letra)

    if qtd_letra > qtd_letra_atual:
        letra_atual = letra
        qtd_letra_atual = qtd_letra
    
    
    i += 1

print(f'A primeira letra que mais repete é a "{letra_atual}" e ela repete {qtd_letra_atual} vezes')

