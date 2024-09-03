def DFS(listaAdj, v):
    visitados = []
    pilha = []
    pilha.append(v)
    while pilha:
        pilha_aux = []
        v_aux = pilha.pop()
        if v_aux not in visitados:
            visitados.append(v_aux)
        for i in (listaAdj[v_aux]):
            if i not in visitados:
                pilha_aux.append(i)
        for i in range(0,len(pilha_aux)):
            pilha.append(pilha_aux.pop())
    for adjacente in (listaAdj):
        if adjacente not in visitados:
            visitados.append(adjacente)

    print (visitados)
    return visitados