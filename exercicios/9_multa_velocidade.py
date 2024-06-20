'''
Nome: Julio Miranda
Data: 06/06/2024
Versão: 1.0
Algoritmo: Multa velocidade
Descrição: Escreva um programa que leia a velocidade máxima permitida em 
           uma avenida e velocidade com que o motorista estava dirigindo nela e 
           calcule a multa que uma pessoa vai receber;
                
                Velocidade Ultrapassada	    Valor da Multa
                Até 10 km/h	                	R$ 50,00
                11 a 30 km/h	           		R$ 100,00
                Mais 31 km/h	            	R$ 200,00
'''
#================================================================
#variaveis
limiteVelocidade = 0
velocidadeMotorista = 0
diferencaVelocidade = 0
valorMulta = ''
#entrada
limiteVelocidade = int(input('Insira a o limite de velocidade da via: '))
velocidadeMotorista = int(input('Insira a velocidade do motorista: '))
#processamento
diferencaVelocidade = velocidadeMotorista - limiteVelocidade

if(diferencaVelocidade > 0 and diferencaVelocidade <=10):
    valorMulta = 'R$50,00'
elif(diferencaVelocidade >= 11 and diferencaVelocidade <=30):
    valorMulta = 'R$100,00'
elif(diferencaVelocidade >= 31):
    valorMulta = 'R$200,00'
else:
    valorMulta = 'R$0,001'
#saida
print(valorMulta)
#================================================================