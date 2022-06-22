import math

#P = piso , G = Grama , A = Areia , F = Floresta  , M = Montanha , R = Rio
caminhoPossivel = ('P','G','A','F','M','R')
custoChao = (10,10,20,100,150,180)
class No():
    def __init__(self,pai=None,posicao=None):
        self.pai = pai
        self.f = 0
        self.h = 0
        self.g = 0
        self.posicao = posicao

    def __eq__(self, other):
        return self.posicao == other.posicao
    
    def custo(self,mapa):
        letra = mapa[self.posicao[1]][self.posicao[0]]
        for i in range(0,len(caminhoPossivel)):
            if (letra == caminhoPossivel[i]):
                custo = custoChao[i]
                return custo



listaFechada = []
listaAberta = []

def buscaCaminho(mapa,inicio,fim):
    tamanhoMapa = len(mapa)

    noInicial = No(posicao=inicio)
    noFinal = No(posicao=fim)

    listaAberta.append(noInicial)

    while listaAberta:
        # print('\n')
        # print(list(map(lambda n: n.posicao,listaAberta)))
        # print(list(map(lambda n: n.posicao,listaFechada)))
        noAtual = listaAberta[0]

        for no in listaAberta:
            if no.f < noAtual.f:
                noAtual = no
            
        listaAberta.remove(noAtual)
        listaFechada.append(noAtual)

        if noAtual == noFinal:
            caminho = []
            no = noAtual
            while no is not None:
                caminho.append(no.posicao)
                no = no.pai
            return caminho[::-1]
        
        filhos = []
        
        x = noAtual.posicao[0]
        y = noAtual.posicao[1]

        if x-1>-1 and mapa[y,x-1] in caminhoPossivel:
            filhos.append(No(noAtual,(x-1,y)))
        if x+1<tamanhoMapa and mapa[y,x+1] in caminhoPossivel:
            filhos.append(No(noAtual,(x+1,y)))
        if y-1>-1 and mapa[y-1,x] in caminhoPossivel:
            filhos.append(No(noAtual,(x,y-1)))
        if y+1<tamanhoMapa and mapa[y+1,x] in caminhoPossivel:
            filhos.append(No(noAtual,(x,y+1)))
        
        for filho in filhos:

            if filho in listaFechada:
                continue
            
            filho.g = noAtual.g + filho.custo(mapa)
            filho.h = calculaHeuristica(filho.posicao, fim)
            filho.f = filho.g+filho.h

            buscaFilho = list(filter(lambda n: n.posicao == filho.posicao and n.g < filho.g,listaAberta))
            if len(buscaFilho) > 0: continue

            

            listaAberta.append(filho)

def calculaHeuristica(posicaoAtual,estadoFinal):
    heuristica = ((posicaoAtual[0] - estadoFinal[0]) ** 2) + ((posicaoAtual[1] - estadoFinal[1]) ** 2)
    return heuristica


