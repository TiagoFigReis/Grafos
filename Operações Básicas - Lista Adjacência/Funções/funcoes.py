import numpy as np

def entrada(instancia):
    caminho = 'C:/Users/tiago/OneDrive/Documentos/Tiago/Ciência da Computação/3º Período/Algoritmos em Grafos/AT3/Instancias/'+instancia+'.txt'
    with open(caminho,'r') as arq:
        data = np.genfromtxt(arq,dtype='int')
    return data
def criaListaAdjacencias(matriz):
    dim = [len(matriz),len(matriz[0])]
    lstadj = {}
    for i in range(0,dim[0]):
        adj = []
        for j in range(0,dim[1]):
            count = matriz[i][j]
            if count>0:
                for k in range(0,count):
                    adj.append(j)
        lstadj[i]=adj
    return lstadj

def tipoGrafoLista(listaAdj):
    dim = len(listaAdj)
    tgrafo = 0
    for i in range(0,dim):
        laux=listaAdj[i]
        dim2 = len(laux)
        for j in range(0,dim2):
            if i not in listaAdj[laux[j]] :
                tgrafo = 1
    for i in range(0,dim):
        if i in listaAdj[i]:
            return 30+tgrafo
    for i in range(0,dim):
        laux = listaAdj[i]
        dim2 = len(laux)
        for j in range(0,dim2):
            if laux.count(laux[j])>1:
                return 20+tgrafo
    return tgrafo
def calcDensidade(listaAdj):
    dim = len(listaAdj)
    arestas = 0
    for i in range(0, dim):
        arestas += len(listaAdj[i])
    densidade = arestas / (dim * (dim - 1))
    return densidade
def insereAresta(listaAdj,vi,vj):
    dim = len(listaAdj)
    laux = []
    for i in range(0,dim):
        laux=listaAdj[i]
        dim2 = len(laux)
        for j in range(0,dim2):
            if i not in listaAdj[laux[j]]:
                k = 0
                while k < len(listaAdj[vi]):
                    if (listaAdj[vi][k] > vj):
                        break
                    k = k + 1
                listaAdj[vi].insert(k, vj)
                return listaAdj
    k = 0
    while k < len(listaAdj[vi]):
        if (listaAdj[vi][k] > vj):
            break
        k = k + 1
    listaAdj[vi].insert(k, vj)
    k = 0
    while k < len(listaAdj[vj]):
        if (listaAdj[vj][k] > vi):
            break
        k = k + 1
    listaAdj[vj].insert(k, vi)
    return listaAdj
def insereVerticeLista(listaAdj):
    dim = len(listaAdj)
    for i in range(0,dim):
        if (i == dim-1):
            listaAdj[i+1]=[]
    return listaAdj

def removeArestaLista(listaAdj, vi, vj):
    dim = len(listaAdj)
    laux = []
    for i in range(0, dim):
        laux = listaAdj[i]
        dim2 = len(laux)
        for j in range(0, dim2):
            if i not in listaAdj[laux[j]]:
                adj = listaAdj[vi]
                if vj in adj:
                    adj.remove(vj)
                    listaAdj[vi] = adj
                    return listaAdj
    adj = listaAdj[vi]
    if vj in adj:
        adj.remove(vj)
        listaAdj[vi] = adj
    adj = listaAdj[vj]
    if vi in adj:
        adj.remove(vi)
        listaAdj[vj] = adj
        return listaAdj
def removeVerticeLista(listaAdj, vi):
    dim = len(listaAdj)
    for i in range(0,dim):
        if vi in listaAdj[i]:
            adj = listaAdj[i]
            count = listaAdj[i].count(vi)
            if count > 0:
                for j in range(0,count):
                    adj.remove(vi)
            listaAdj[i]=adj
    listaAdj.pop(vi, None)
    return listaAdj
def verificaAdjacenciaLista(listaAdj,vi,vj):
    if vj in listaAdj[vi]:
        return True
    else:
        return False