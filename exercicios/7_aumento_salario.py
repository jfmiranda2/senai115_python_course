'''
Algoritmo "Aumento de salário"
Autor: Julio Miranda
Data: 04/06/2024
Descrição   : Faça um programa que receba o salário de um funcionário, calcule e mostre o
              novo salário, sabendo-se que:
                Salário < R$ 1000,00 aumento de 25%.
                Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
                Salário >= R$ 2000,00 aumento de 10%.

'''
#============================================================
#variaveis
salario = 0
salario_aumento = 0
#entrada
salario = float(input('Por favor, insira o seu salário:'))
#processamento
if(salario < 1000):
    salario_aumento = salario * 1.25
    print(round(salario_aumento))
elif(salario >= 1000 and salario < 2000): #as duas condições tem que ser verdadeiras
    salario_aumento = salario * 1.15
    print(round(salario_aumento))
elif(salario >=2000):
    salario_aumento = salario * 1.1
    print(round(salario_aumento))
#saida
#============================================================
