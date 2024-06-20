'''
Descrição   : Faça um programa que receba dois valores, sendo que o 
              primeiro deve ser menor que o segundo. 
              O programa deve apresentar todos os números ímpares 
              contidos nesta sequência. 
              (Modulo %. Exemplo: 7%2 = 1)
'''
#===================================================================
num_A = 0
num_B = 0

num_A = int(input('Insira o valor inicial do seu range: '))# 5
num_B = int(input('Insira o valor final para o seu range: ')) # 10

#for alguma_cois in range(5, 10):
for nr_dentro_range in range(num_A, num_B): # 5 -> 6 -> 7 -> 8 -> 9
    resto = nr_dentro_range % 2 # 0(par) ou 1(ímpar)
    #print(f'{nr_dentro_range} % 2 = {resto}')
    if resto == 1:
        print(nr_dentro_range)
#===================================================================