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


def ordenacaoTopologica(listaAdj):
    visitados = []
    tempo = 0
    tempoD = {}
    tempoT = {}
    for i in listaAdj:
        if i not in visitados:
            tempo = deepFirstReach(listaAdj, i, visitados, tempoD, tempoT, tempo)
    ordem_topologica = []
    while len(tempoT):
        maior = list(tempoT.keys())[0]
        for i in tempoT:
            if tempoT[i] > tempoT[maior]:
                maior = i
        ordem_topologica.append(maior)
        tempoT.pop(maior)
    print(ordem_topologica)
    return ordem_topologica