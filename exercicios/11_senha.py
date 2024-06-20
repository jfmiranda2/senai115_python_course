
'''
Data: 07/06/2024
Versão: 1.0
Algoritmo: Senha
Descrição: Faça um programa que solicite para o usuário a senha de acesso 
            ao sistema, ele terá no máximo três tentativas para inserir a correta
            cadastrada (senai115), caso passe desse limite uma mensagem de erro deve
            aparecer. 
'''
#========================================================
senha = '' #var para receber a senha do usuario
senhaPadrao = 'senai115' #senha padrão do sistema
tentativas = 3 #numero de tentativas de acesso ao sistema
while True:
    senha = input('Digite a sua senha: ') 
    #senai115 => numeros com letras então sem casting
    if senha == senhaPadrao:
        print('Acesso liberado!')
        break #quebra o loop while, ou seja finaliza o programa
    else:
        tentativas = tentativas - 1 # tentativas -= 1
        print('Você só possui mais', tentativas, 'tentativas')
    if tentativas <= 0:
        print('Sistema bloqueado')
        break
#========================================================