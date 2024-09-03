import numpy as np
def tipoGrafo(matriz):
    tgrafo=0
    dim=[len(matriz),len(matriz[0])]
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            if matriz[i][j] != matriz[j][i]:
                tgrafo = 1
                break
    for i in range(0, dim[0]):
        if matriz[i][i]>0:
            return 30+tgrafo
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            if matriz[i][j]>1:
                return 20+tgrafo
    return tgrafo
def verificaAdjacencia(matriz, vi, vj):
    return (matriz[vi][vj]>0)
def calcDensidade(matriz):
    densidade=0
    dim = [len(matriz), len(matriz[0])]
    arestas = 0
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            arestas += matriz[i][j]
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            if matriz[i][j] != matriz[j][i]:
                densidade = (arestas) / (dim[1] * (dim[1] - 1))
                return densidade
    densidade = (2 * arestas / 2) / (dim[1] * (dim[1] - 1))
    return densidade
def insereVertice(matriz):
    matriz = np.pad(matriz,(0,1),constant_values=0)
    return matriz

def insereAresta(matriz,vi,vj):
    dim = [len(matriz),len(matriz[0])]
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            if(matriz[i][j] != matriz[j][i]):
                matriz[vi][vj] += 1
                return matriz
    if(vi!=vj):
        matriz[vi][vj]+=1
        matriz[vj][vi]+=1
    else:
        matriz[vj][vi] += 1
    return matriz
def removeAresta(matriz,vi,vj):
    dim = [len(matriz),len(matriz[0])]
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            if (matriz[i][j] != matriz[j][i] and matriz[vi][vj] > 0 ):
                    matriz[vi][vj] -= 1
                    return matriz
    if(matriz[vi][vj]>0 and vi != vj ):
            matriz[vi][vj] -= 1
            matriz[vj][vi] -= 1
    else:
            matriz[vj][vi] -= 1
    return matriz
def removeVertice(matriz,vi):
    dim = [len(matriz), len(matriz[0])]
    for j in range(0,dim[0]):
        matriz[j][vi]=-1
    for j in range(0,dim[1]):
        matriz[vi][j] = -1
    return matriz