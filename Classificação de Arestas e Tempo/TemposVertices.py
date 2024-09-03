def temposVertices (listaAdj, vertice):
    visitados = []
    tempo = 0
    tempoD = {}
    tempoT = {}
    tempo = deepFirstReach(listaAdj, vertice, visitados, tempoD, tempoT, tempo)
    for i in listaAdj:
        if i not in visitados:
            tempo = deepFirstReach(listaAdj, i, visitados, tempoD, tempoT, tempo)
    temposVertice = {}
    for i in listaAdj:
        temposVertice[i] = str(tempoD[i]) + "/" + str(tempoT[i])
    print (temposVertice)
    return temposVertice


def deepFirstReach(listaAdj, v, visitados, tempoD, tempoT, tempo):
    visitados.append(v)
    tempo += 1
    tempoD[v] = tempo
    for adjacente in listaAdj[v]:
        if adjacente not in visitados:
            tempo = deepFirstReach(listaAdj, adjacente, visitados, tempoD, tempoT, tempo)
    tempo += 1
    tempoT[v] = tempo
    return tempo