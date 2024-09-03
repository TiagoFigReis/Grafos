def bellmanFord(matriz, vOrigem, vDestino):
    custo = [float('inf')] * len(matriz)
    rota = [0] * len(matriz)
    custo[vOrigem] = 0
    for i in range(0, len(matriz)-1):
        for j in range(0, len(matriz)):
            for k in range(0, len(matriz[j])):
                if custo[k] > custo[j] + matriz[j][k] and matriz[j][k] != -1:
                    custo[k] = custo[j] + matriz[j][k]
                    rota[k] = j
    for j in range(0, len(matriz)):
        for k in range(0, len(matriz[j])):
            if custo[k] > custo[j] + matriz[j][k] and matriz[j][k] != -1:
                print(False)
                return False
    sequencia = []
    vertice_aux = vDestino
    while vertice_aux != vOrigem:
        sequencia.insert(0, vertice_aux)
        vertice_aux = rota[vertice_aux]
    sequencia.insert(0, vertice_aux)
    print(sequencia,custo[vDestino])
    return sequencia,custo[vDestino]
