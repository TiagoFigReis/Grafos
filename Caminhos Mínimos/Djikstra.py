def menorcusto(custo, Fechados, Abertos):
    menor = Abertos[0]
    for i in Abertos:
        if custo[i] < custo[menor]:
            menor = i
    return menor

def dijkstra(matriz, vOrigem, vDestino):
    custo = [float('inf')] * len(matriz)
    rota = [vOrigem] * len(matriz)
    custo[vOrigem] = 0
    Abertos = []
    for i in range (len(matriz)):
        Abertos.append(i)
    Fechados = []
    while len(Abertos) > 1:
        v = menorcusto(custo,Abertos)
        Fechados.append(v)
        Abertos.remove(v)
        Adjacentes = []
        for i in range (len(matriz)):
            if matriz[v][i] > 0:
                Adjacentes.append(i)
        Adjacentes = [adjacentes for adjacentes in Adjacentes if adjacentes != Fechados]
        for i in Adjacentes:
            if custo[v] + matriz[v][i] < custo[i]:
                rota[i] = v
                custo[i] = custo[v] + matriz[v][i]
    vertice_aux = vDestino
    sequencia = []
    while vertice_aux != vOrigem:
        sequencia.insert(0, vertice_aux)
        vertice_aux = rota[vertice_aux]
    sequencia.insert(0, vOrigem)
    print(sequencia, custo[vDestino])
    return sequencia, custo[vDestino]

dijkstra([[0, 3, 8, 4, -1, 10], [ 3, 0, -1, 6, -1, -1], [ 8, -1, 0, -1, 7, -1], [ 4,  6, -1, 0,  1,  3], [-1, -1,  7,  1, 0, 1], [10, -1, -1,  3,  1, 0]], 0, 5)