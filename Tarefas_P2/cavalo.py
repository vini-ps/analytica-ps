lin = ['8','7','6','5','4','3','2','1']
col = ['a','b','c','d','e','f','g','h']
tabuleiro = [[],[],[],[],[],[],[],[]]


def cria_tabuleiro():
    for i in range(len(lin)):
        for j in range(len(col)):
            tabuleiro[i].append(col[j]+lin[i])
    return tabuleiro

def movimentar(pos):
    index_linha = lin.index(pos[1])
    index_colun = col.index(pos[0])
    mov = [(1,2),(2,1),(1,-2),(2,-1)]    #lista com alguns movimentos
    resp = []
    #loop para tentar movimentar o cavalo a partir da posição escolhida
    for i in range(4):
        try:
            nova_pos = tabuleiro[abs(index_linha + mov[i][0])][abs(index_colun + mov[i][1])]
            resp.append(nova_pos)
        except IndexError:
            break
    for i in range(4):
        try:
            nova_pos = tabuleiro[abs(index_linha+(-mov[i][0]))][abs(index_colun+(-mov[i][1]))]
            resp.append(nova_pos)
        except IndexError:
            break
        
    return resp

def main():
    while True:
        posicao = input("posicao: ")
        if posicao == 'f':
            print('Saindo...')
            exit()
        elif len(posicao) != 2:
            print('input inválido')
        elif posicao[0] not in col or posicao[1] not in lin:
            print('input inválido')
        else:
            break
    
    tabuleiro = cria_tabuleiro()
    
    lista = movimentar(posicao)
    
    resposta = list(set(lista))
    
    resposta.sort()
    
    print(resposta)

main()
