'''
Descrição: Faça um Jogo da velha
'''
idosa = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
        ]

linha_complementar = '--- ' + '---' + ' ---' 
for linha in range(3):
    linha_completa = ''
    for coluna in range(3):
        #soma = soma + 1 -> soma += 1
        #linha_completa = linha_completa + idosa[linha][coluna] + ' | '
        if coluna < 2:
            linha_completa += idosa[linha][coluna] + ' | ' 
        else:
            linha_completa += idosa[linha][coluna]
    print(f' {linha_completa}')
    if linha < 2:
        print(linha_complementar)