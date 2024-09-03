def BFS(listaAdj, v):
    Q = []
    analisado = []
    Q.append(v)
    while Q:
        v = Q.pop(0)
        for i in listaAdj[v]:
            if (i not in Q) and (i not in analisado):
                Q.append(i)
        analisado.append(v)
    for i in listaAdj:
        if i not in analisado:
            analisado.append(i)
    print (analisado)
    return analisado