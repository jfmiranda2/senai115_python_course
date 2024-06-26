'''
Descrição: Faça um Jogo da velha
'''
idosa = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]
rodadas = 0
jogador = 'X'
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
    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('posicao não encontrada')
   