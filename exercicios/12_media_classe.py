'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 4 e 7 	    Exame
                    De 8 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''
aluno = 0
qtdAlunos = 6
alunosAprovado = 0
alunosReprovados = 0
alunosExame = 0
somaMedia = 0
mediaFinal = 0

while aluno < qtdAlunos:
    aluno = aluno + 1 # aluno += 1
    #Aluno x
    nota_um = 0
    nota_dois = 0
    media = 0
    #nota_um = float(input('Insira a nota 1 do aluno',aluno,':'))
    nota_um = float(input(f'Insira a nota 1 do aluno {aluno}: '))
    nota_dois = float(input(f'Insira a nota 2 do aluno {aluno}: '))

    media = (nota_um + nota_dois)/2 # 10 -> 8 -> 5 -> 10 -> 7 -> 8
    somaMedia = somaMedia + media # 10 -> 18 -> 23 -> 33 -> 40 -> 48

    if(media <= 3):
        print('Reprovado')
        alunosReprovados += 1 #alunosReprovados = alunosReprovados + 1
    elif(media >= 4 and media <= 7):
        print('Exame')
        alunosExame += 1 #alunosExame = alunosExame + 1
    else:
        print('Aprovado')
        alunosAprovado +=1 #alunosAprovado = alunoAprovado + 1

mediaFinal = round((somaMedia / qtdAlunos),2)
print(f'Media final da turma: {mediaFinal}')
print(f'Quantidade de alunos aprovados: {alunosAprovado}')
print(f'Quantidade de alunos reprovados: {alunosReprovados}')
print(f'Quantidade de alunos exame: {alunosExame}')
