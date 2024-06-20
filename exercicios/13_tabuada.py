'''
Autor: Julio Miranda
Data: 13/06/2024
Algoritmo "Tabuada"
Descrição: Faça um programa que calcule a tabuada de um número digitado 
            pelo usuário;
'''
#============================================================
numero = 0
resultado = 0

numero = int(input('Digite um número: '))

for i in range(11): #i < 11 ( 0 até 10 )
    #resultado =  numero * i
    print(f'{numero} x {i} = {numero * i}') #interpolação f(format)
    #print(numero,'x',i,'=',resultado)
#============================================================