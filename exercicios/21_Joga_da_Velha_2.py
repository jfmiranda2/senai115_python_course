'''
Descrição: Faça um Jogo da velha
'''
idosa = [['1','2','3'], ## print(idosa[1][1]]) => '5'
         ['4','5','6'],
         ['7','8','9']]
rodadas = 0
jogador = 'X'

#função mostrar o vencedor
def mostrar_vencedor(vencedor):#vencedor escopo local da função
    print('Temos um vencedor', vencedor)

while rodadas < 9:
    posicao = input(f'jogador {jogador} escolha uma posição:')
    posicao_encontrada = False
    for linha in range(3):
        linha_completa = ''
        for coluna in range(3):
            if posicao == idosa[linha][coluna]:
                idosa[linha][coluna] = jogador
                posicao_encontrada = True
            linha_completa += idosa[linha][coluna] + ' | ' 
        print(f' {linha_completa}')

    #verificar se tem vencedor
    if(idosa[0][0] == idosa[0][1] == idosa[0][2] or
       idosa[1][0] == idosa[1][1] == idosa[1][2] or
       idosa[2][0] == idosa[2][1] == idosa[2][2] or
       idosa[0][0] == idosa[1][0] == idosa[2][0] or
       idosa[0][1] == idosa[1][1] == idosa[2][1] or
       idosa[0][2] == idosa[1][2] == idosa[2][2] or
       idosa[0][0] == idosa[1][1] == idosa[2][2] or
       idosa[0][2] == idosa[1][1] == idosa[2][0]):
        mostrar_vencedor(jogador)
        houve_vencedor = True
        break
    else:
        houve_vencedor = False

    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('posicao não encontrada')
#fim while

if(houve_vencedor == False):
    print('Ocorreu uma idosa')