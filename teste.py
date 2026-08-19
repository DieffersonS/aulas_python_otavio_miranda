perguntas = [
    {
        'Pergunta':'Quanto é 2 + 2?',
        'Opções':['1','2','4','5'],
        'Resposta':'4',
    },
    {
        'Pergunta':'Quanto é 5 x 5?',
        'Opções':['25','55','10','51'],
        'Resposta':'25',
    },
    {
        'Pergunta':'Quanto é 10 ÷ 2?',
        'Opções':['4','5','2','1'],
        'Resposta':'5',
    },
]

for i in perguntas:
    for y in i['Opções']:
        print(y)