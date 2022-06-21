import math
from arquivos import getDungeons


arrayCaminho = ()

def buscaCaminho(map,estadoInicial,estadoFinal):
    posicao = estadoInicial
    while posicao != estadoFinal:
        arrayCaminho.append(posicao)
        filhos = testeFilhos(posicao,map)
        posicao = testeMenorCusto(posicao,filhos,estadoFinal)

def testeFilhos(posicao,map,arrayCaminho):
    possivel = ()
    x = posicao[0]
    y = posicao[1]
    cima = map[x][y+1]
    baixo = map[x][y-1]
    direita = map[x+1][y]
    esquerda = map[x-1][y]
    if(cima == 'F' and (cima not in arrayCaminho)):
        possivel.append(cima)
    if(baixo == 'F' and (baixo not in arrayCaminho)):
        possivel.append(baixo)
    if(esquerda == 'F' and (esquerda not in arrayCaminho)):
        possivel.append(esquerda)
    if(direita == 'F' and (direita not in arrayCaminho)):
        possivel.append(direita)
    return possivel


def testeMenorCusto(posicao,filhos,estadoFinal):
    custo = calculaDistancia(posicao,filhos[0]) + calculaHeuristica(filhos[0],estadoFinal)
    for i in range(0,len(filhos)):
        custoDist = calculaDistancia(posicao,filhos[i])
        custoHeurist = calculaHeuristica(filhos[i],estadoFinal)
        if(custo > (custoDist +custoHeurist)):
            custo = (custoDist +custoHeurist)
            estadoDestino = filhos[i]
    return estadoDestino
    
    


def calculaDistancia(posicaoAtual,posicaoDestino):
    custo = math.sqrt( (posicaoDestino[0]-posicaoAtual[0])**2 + (posicaoDestino[1] - posicaoAtual[1])**2 )
    return custo

def calculaHeuristica(posicaoAtual,estadoFinal):
    heuristica = math.sqrt( (estadoFinal[0]-posicaoAtual[0])**2 + (estadoFinal[1] - posicaoAtual[1])**2 )
    return heuristica