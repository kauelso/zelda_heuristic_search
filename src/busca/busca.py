import math

#P = piso , G = Grama , A = Areia , F = Floresta  , M = Montanha , R = Rio
caminhoPossivel = ('W','P','G','A','F','M','R')
custoChao = (999999,10,10,20,100,150,180)

listaFechada = []
listaAberta = []

listaValores = []
listaValores_pais = []

custoTotal = 0
arrayCaminho = []
arrayCustos = []


def buscaCaminho(map,estadoInicial,estadoFinal):
    index = 0
    posicao = estadoInicial
    
    listaFechada.append(posicao)
    listaValores.append(index)
    listaValores_pais.append(index)
    index+=1
    filhos = testeFilhos(posicao,map,listaFechada)

    for i in range(0,len(filhos)):
        listaAberta.append(filhos[i])

    while listaAberta:
        # print(listaFechada)
        # print('\n')
        # print(listaAberta)
        # print('\n')
        posicaonova = testeMenorCusto(listaAberta,estadoFinal,map)
        listaAberta.remove(posicaonova)
        listaFechada.append(posicaonova)
        listaValores.append(index)
        index+=1
        for i in range(0,len(listaFechada)):
            if(listaFechada[i] == posicao):
                listaValores_pais.append(listaValores[i])
        filhos = testeFilhos(posicaonova,map,listaFechada)
        for filho in filhos:
            listaAberta.append(filho)

    caminhoReverso = len(listaFechada)
    while caminhoReverso != estadoInicial:
        arrayCaminho.append(caminhoReverso)
        for i in range(0,len(listaValores)):
            if(listaValores[i] == caminhoReverso):
                pai = listaValores_pais[i]
                caminhoReverso = listaFechada[pai]

    return arrayCaminho


def testeFilhos(posicao,map,listaFechada):
    possivel = []
    x = posicao[0]
    y = posicao[1]
    cima = map[y][x+1]
    baixo = map[y][x-1]
    direita = map[y+1][x]
    esquerda = map[y-1][x]
    if(cima in caminhoPossivel and ((x+1,y) not in listaFechada)):
        possivel.append((x+1,y))
    if(baixo in caminhoPossivel and ((x-1,y) not in listaFechada)):
        possivel.append((x-1,y))
    if(esquerda in caminhoPossivel and ((x,y+1) not in listaFechada)):
        possivel.append((x,y+1))
    if(direita in caminhoPossivel and ((x,y-1) not in listaFechada)):
        possivel.append((x,y-1))
    return possivel


def testeMenorCusto(filhos,estadoFinal,map):
    custo = custoPiso(filhos[0],map) + calculaHeuristica(filhos[0],estadoFinal)
    estadoDestino = filhos[0]
    for i in range(0,len(filhos)):
        custoDist = custoPiso(filhos[i],map)
        custoHeurist = calculaHeuristica(filhos[i],estadoFinal)
        if(custo > (custoDist + custoHeurist)):
            custo = (custoDist + custoHeurist)
            estadoDestino = filhos[i]
    return estadoDestino

def custoPiso(filho,map):
    letra = map[filho[1]][filho[0]]
    for i in range(0,len(caminhoPossivel)):
        if (letra == caminhoPossivel[i]):
            custo = custoChao[i]
            return custo


def calculaHeuristica(posicaoAtual,estadoFinal):
    heuristica = math.sqrt( (estadoFinal[0]-posicaoAtual[0])**2 + (estadoFinal[1] - posicaoAtual[1])**2 )
    return heuristica
