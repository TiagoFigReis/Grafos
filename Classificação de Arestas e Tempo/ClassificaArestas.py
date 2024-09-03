def DFS(listaAdj, v, visitados, tempoD, tempoT, tempo, cor):
    visitados.append(v)
    cor[v] = "cinza"
    tempo += 1
    tempoD[v] = tempo
    for adjacente in listaAdj[v]:
        if cor[adjacente] == "branco":
            print(str(v) + " " + str(adjacente) + " Tree")
        elif cor[adjacente] == "cinza":
            print(str(v) + " " + str(adjacente) + " Back")
        else:
            if tempoD[v] > tempoD[adjacente]:
                print(str(v) + " " + str(adjacente) + " Cross")
            else:
                print(str(v) + " " + str(adjacente) + " Forward")
        if adjacente not in visitados:
            tempo = DFS(listaAdj, adjacente, visitados, tempoD, tempoT, tempo, cor)
    cor[v] = "preto"
    tempo += 1
    tempoT[v] = tempo
    return tempo

def classificaArestas (listaAdj, vertice):
    visitados = []
    tempo = 0
    tempoD = {}
    tempoT = {}
    cor = {}
    for i in listaAdj:
        cor[i] = "branco"
    tempo = DFS(listaAdj, vertice, visitados, tempoD, tempoT, tempo, cor)
    for i in listaAdj:
        if i not in visitados:
            tempo = DFS(listaAdj, i, visitados, tempoD, tempoT, tempo, cor)
    return