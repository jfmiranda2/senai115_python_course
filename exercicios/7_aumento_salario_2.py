'''
Autor: Julio Miranda
Data: 06/06/2024
Versão: 2.0
Algoritmo "Aumento de salário"
Descrição   : Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que:
                Salário < R$ 1000,00 aumento de 25%.
                Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
                Salário >= R$ 2000,00 aumento de 10%.
'''
#================================================================
#variaveis
salario = 0 #camel style
salarioAumento = 0
porcentagem = ''

#entrada
salario = float(input('Insira o salário do funcionário: '))
#processamento
if(salario < 1000):
    porcentagem = '25%'
    salarioAumento = salario * 1.25
elif(salario >= 1000 and salario < 2000):  
    porcentagem = '15%'
    salarioAumento = salario * 1.15
elif(salario >= 2000):
    porcentagem = '10%'
    salarioAumento = salario * 1.1
salarioAumento = round(salarioAumento, 2)#função nativa do python para arredondar os 
                                         #valores
#saida
print('O seu salario de',salario,'sofre um reajuste de', porcentagem, 
      'sendo agora no valor de',salarioAumento)
#================================================================