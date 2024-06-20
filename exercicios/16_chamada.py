'''
Descrição   : Faça um programa que receba o número da chamada dos alunos
              do curso de python no período noturno do SENAI 115 e apresente
              o seu nome
'''
#===================================================================
alunos_python_senai = [
    'Luana', 'Gustavo', 'Danielle',
    'Felipe', 'João mudou de lugar','Thiago',
    'Vitor', 'José', 'Arthur', 'Pedrão',
    'Mauricio', 'Davi', 'Kawan',
    'Andrey', 'Lucas', 'Diego matrix',
    'João Timão', 'Ana', 'Vinicius vascaino',
    'Adriel', 'Patrick','Brunão',
    'Professor girafalles mini'
]

while True:
    nr_chamada = 0
    nr_chamada = int(input('Digite o número da chamada: '))
    print(alunos_python_senai[nr_chamada])

    continuar = input('Digite S para sair e C para continuar:')
    if continuar == 'S':
        break