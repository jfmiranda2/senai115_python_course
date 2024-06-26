'''

Autor: Julio Miranda
Data: 25/06/2024
Versão: 1.0
Descrição: Estudo do tipo de dado Array(Vetor)

'''

# alunos_sala = ['Luana', 'Gustavo','Danielle']

# alunos_sala.append('Felipe')
# print(alunos_sala)

# print(alunos_sala[2]) # indice 2 -> Danielle

# for indice in range(4):
#     print(alunos_sala[indice])

# for aluno in alunos_sala:
#     print(aluno)

          #    0       1        2
cabecalho = ['Nome','Idade','Matricula']
          #   0        1      2
dado_um   = ['Pele','Eterno','10']

print(dado_um[0]) # -> Pele
#=============================================================
#Matriz -> um array com arrays dentro
        #     0        1
tabela = [cabecalho, dado_um]
print(tabela[1][0]) # -> Pele

#[       0       1          2
#  0  ['Nome','Idade ','Matricula'],
#  1  ['Pele','Eterno','    10   ']
#]
#coordenas  [l][c] l=linha c=coluna
print(tabela[0][1]) # -> Idade
print(tabela[1][2]) # -> 10