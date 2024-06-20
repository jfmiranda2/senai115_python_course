'''
Autor: Julio Miranda
Data: 07/06/2024
Versão: 1.0
Descrição: Estudo da estrutura de repetição "While"

'''
'''
#============================================================
indice = 1
while indice <= 6:
    print('indice: ')
    indice = indice + 1 #indice += 1
#============================================================
indice_2 = 10
while indice_2 > 0:
    print(indice_2, 'Julio')
    indice_2 = indice_2 - 1
#============================================================
indice_3 = 1
while True:
    print(indice_3)
    indice_3 = indice_3 + 1
    if indice_3 == 5:
        break
#============================================================
'''
# indice_4 = 1
while True:
    opcao = input('Digite S para finalizar o programa')
    # indice_4 = indice_4 + 1
    if(opcao == 'S'):
        break

