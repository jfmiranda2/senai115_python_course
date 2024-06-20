'''
Autor: Julio Miranda
Data: 13/06/2024
Algoritmo "Tabuada 1 ao 10"
Descrição: Faça um programa que apresente a tabuado 1 ao 10;
'''
#============================================================
print('--------------------------------')
for l in range(11): # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    for c in range(11): # 0 -> 10
        print(f'{l} x {c} = {l * c}')
    print('--------------------------------')
#============================================================