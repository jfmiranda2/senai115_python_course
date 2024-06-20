
'''
Autor: Julio Miranda
Data: 14/06/2024
Versão: 1.0
Descrição: Estudo do tipo de dado Array
'''
#===================================================================
aluno_a = 'João'
aluno_b = 'Maria'
aluno_c = 'Francisco'
aluno_d = 'Sofia'
aluno_e = 'Milton'
aluno_f = 'Joana'

#array
#            =    0      1        2          3        4         5
turma_python = ['João', 200, 'Francisco', aluno_d, 'Milton', 'Joana'] 

#print(turma_python)
turma_python[1] = 'Maria'
print(turma_python)
print(f'posição 0 do vetor turma_python é igual {turma_python[0]}')
print(f'posição 1 do vetor turma_python é igual {turma_python[1]}')
print(f'posição 2 do vetor turma_python é igual {turma_python[2]}')
print(f'posição 3 do vetor turma_python é igual {turma_python[3]}')
print(f'posição 4 do vetor turma_python é igual {turma_python[4]}')
print(f'posição 5 do vetor turma_python é igual {turma_python[5]}')

#===================================================================
#                        0  1  2  3  4  5   
alunos_python_noturno = [4, 5, 3, 2, 0, 1]
print(alunos_python_noturno) #array velho
alunos_python_noturno[0] = 'Joana'
alunos_python_noturno[1] = 'Milton'
alunos_python_noturno[2] = 'Sofia'
alunos_python_noturno[3] = 'Francisco'
alunos_python_noturno[4] = 'Maria'
alunos_python_noturno[5] = 'João'
print(alunos_python_noturno[3]) #array novo
