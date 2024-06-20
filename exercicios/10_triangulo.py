'''
Nome: Julio Miranda
Data: 07/06/2024
Algoritmo "Tipo triângulo"
Descrição: Faça um programa que receba 3 valores e verifique se eles podem 
representar os lados em um triângulo;

1: Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.

2: Triângulos isósceles: triângulo que possui dois lados com medidas iguais.

3: Triângulo equilátero: triângulo que possui todos os lados com medidas iguais.

Lembrando que a soma das medidas de dois lados de um triângulo é sempre maior que a medida do 
terceiro lado.
'''
#============================================================
#variaveis
lado_a = 0
lado_b = 0
lado_c = 0
tipo_triagulo = ''
#entrada
#Ctrl+ Alt + Shift + (direcionais up ou down)
lado_a = int(input('Insira o valor do lado a: '))
lado_b = int(input('Insira o valor do lado b: '))
lado_c = int(input('Insira o valor do lado c: '))
#processamento
if((lado_a + lado_b) > lado_c and 
   (lado_a + lado_c) > lado_b and 
   (lado_b + lado_c) > lado_a and 
    lado_a > 0 and lado_b > 0 and lado_c > 0):
    print('Triângulo Existe')
    if(lado_a == lado_b and lado_b == lado_c):#lado_a == lado_b == lado_c
        tipo_triagulo = 'equilátero'
    elif(lado_a == lado_b or lado_a == lado_c or lado_b == lado_c): 
        #como existiu a verificação no if anterior que um dos lados não são iguais, 
        #não existe a necessidade da verificação do terceiro lado como diferente.
        tipo_triagulo = 'isósceles'
    elif((lado_a != lado_b) and 
         (lado_a != lado_c) and 
         (lado_b != lado_c)):
        tipo_triagulo = 'escaleno'
else:
    print('Triângulo não existe')
#saida
print(tipo_triagulo)
#============================================================