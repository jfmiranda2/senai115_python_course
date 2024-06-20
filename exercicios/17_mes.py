'''
Descrição   : Faça um programa que receba o número do mês e apresente ele por
            extenso:
            !Sem utilizar condicional!
            if mes == 0
                print('Mes não existe')
            else if mes == 1
                print('Janeiro')
'''

meses_ano = ['', 'Janeiro', 'Fevereiro', 
             'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 
             'Novembro', 'Dezembro']

nr_mes = int(input('Digite o numero do mes: '))
print(meses_ano[nr_mes])

