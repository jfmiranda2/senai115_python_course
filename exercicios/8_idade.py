'''
Autor: Julio Miranda
Data: 06/06/2024
Versão: 1.0
Algoritmo "Classificação idade"
Descrição   : Escreva um programa que leia a idade de um indivíduo e 
              escreva a faixa etária a que pertence, de acordo com a tabela abaixo;

              Faixa etária	    Classificação
                  <=12	      	Criança
                    13 ~ 17		Adolescente
                    18 ~ 59	  	Adulto
'''
#================================================================
#variaveis
idade = 0 #inteiro zero
classificacao = '' #string vazia
#entrada
idade = int(input('Insira a sua idade: '))
#processamento
if(idade >= 0 and idade <= 12):
    classificacao = 'Criança'
elif(idade >= 13 and idade <= 17): # and = e
    classificacao = 'Adolescente'
elif(idade >=18 and idade <= 59):
    classificacao = 'Adulto'
elif(idade > 59):
    classificacao = 'Adulto plus'
else:
    classificacao = 'Idade inserida inválida'
#saida
print(classificacao)
#================================================================