"""
Exercício - Sistema de perguntas e respostas
"""
import os

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

acertos = 0
erros = 0
alternativas = 1

print(f'Responda as perguntas:')
for questao in perguntas:
    print(questao['Pergunta'])
    for opcao in questao['Opções']:
        print(f'{alternativas})', opcao)
        alternativas += 1
    resposta = input(f'Resposta: ')
    if resposta == questao['Resposta']:
        acertos += 1
        alternativas = 1
    else:
        erros += 1
        alternativas = 1
    os.system('clear')

print(f'Você teve:\nAcertos: {acertos}\nErros: {erros}')
if acertos < 2:
    print(f'Precisa esturdar mais.')
elif acertos > 2:
    print(f'Parabéns! Acertou tudo!.')
else:
    print(f'Não desanime, você foi bem!.')