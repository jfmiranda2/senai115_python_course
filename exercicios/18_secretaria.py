'''
Descrição   : Faça um programa que adicione alunos ao sistema da escola 
              (array) ou remova um aluno especifico.
              Nesse sistema deve estar previsito um menu com três opções:
              #===================================
              Sistema SENAI
              1 - Adicionar aluno:
              2 - Remover aluno:
              3 - Apresentar alunos
              4 - Sair
              Insira a opção desejada: 
              #===================================   
              Adicionar aluno
              Insira o nome do aluno:
              #===================================   
              Remover aluno
              Insira o nome do aluno para ser removido:
              #===================================   
              Alunos no sistema
              ['João', 'Pedro','Luana']
              #===================================   
'''
opcao = 0 #numero
sistema_alunos = [] #array
novo_aluno = '' #string
while True:
    print('=-'*30) #multiplica a string "=-" 30 vezes
    print('Sistema SENAI')
    print('1 - Adicionar aluno')
    print('2 - Remover aluno')
    print('3 - Apresentar alunos')
    print('4 - Sair')
    opcao = int(input('Insira a opção desejada:'))
    if(opcao == 1):
        print('=-'*30)
        print('Adicionar aluno')
        novo_aluno = input('Digite o nome do novo aluno:')
        sistema_alunos.append(novo_aluno)
    elif(opcao == 2):
        print('=-'*30)
        print('Excluir aluno')
        delete_aluno = input('Digite o nome do aluno para ser deletado:')
        sistema_alunos.remove(delete_aluno)
    elif(opcao == 3):
        print('=-'*30)
        print('Alunos no sistema:')
        print(sistema_alunos)
    else:
        print('Saindo ...')
        break

