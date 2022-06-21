import math
from arquivos import getDungeons

#P = piso , G = Grama , A = Areia , F = Floresta  , M = Montanha , R = Rio
caminhoPossivel = ('P','G','A','F','M','R')
custoChao = (0,10,20,100,150,180)


custoTotal = 0
arrayCaminho = ()
arrayCustos = ()

def buscaCaminho(map,estadoInicial,estadoFinal):
    posicao = estadoInicial
    while posicao != estadoFinal:
        arrayCaminho.append(posicao)
        filhos = testeFilhos(posicao,map)
        posicaonova = testeMenorCusto(posicao,filhos,estadoFinal)
        custo = calculaDistancia(posicao,posicaonova)
        arrayCustos.append(custo)
        custoTotal = custoTotal + custo
        posicao = posicaonova
    print (custoTotal)
    return arrayCaminho,arrayCustos

def testeFilhos(posicao,map,arrayCaminho):
    possivel = ()
    x = posicao[0]
    y = posicao[1]
    cima = map[x][y+1]
    baixo = map[x][y-1]
    direita = map[x+1][y]
    esquerda = map[x-1][y]
    if(cima in caminhoPossivel and (cima not in arrayCaminho)):
        possivel.append(cima)
    if(baixo in caminhoPossivel and (baixo not in arrayCaminho)):
        possivel.append(baixo)
    if(esquerda in caminhoPossivel and (esquerda not in arrayCaminho)):
        possivel.append(esquerda)
    if(direita in caminhoPossivel and (direita not in arrayCaminho)):
        possivel.append(direita)
    return possivel


def testeMenorCusto(posicao,filhos,estadoFinal):
    custo = calculaDistancia(posicao,filhos[0]) + calculaHeuristica(filhos[0],estadoFinal)
    for i in range(0,len(filhos)):
        custoDist = calculaDistancia(posicao,filhos[i])
        custoHeurist = calculaHeuristica(filhos[i],estadoFinal)
        if(custo > (custoDist + custoHeurist)):
            custo = (custoDist + custoHeurist)
            estadoDestino = filhos[i]
    return estadoDestino

def custoPiso(filho):
    letra = map[filho[0]][filho[1]]
    for i in range(0,len(caminhoPossivel)):
        if (letra == caminhoPossivel[i]):
            custo = custoChao[i]
            return custo


def calculaDistancia(posicaoAtual,posicaoDestino):
    custo = math.sqrt( (posicaoDestino[0]-posicaoAtual[0])**2 + (posicaoDestino[1] - posicaoAtual[1])**2 ) + custoPiso(posicaoDestino)
    return custo

def calculaHeuristica(posicaoAtual,estadoFinal):
    heuristica = math.sqrt( (estadoFinal[0]-posicaoAtual[0])**2 + (estadoFinal[1] - posicaoAtual[1])**2 )
    return heuristica