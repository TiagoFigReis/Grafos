def DFS(listaAdj, v, visitados, cor):
    visitados.append(v)
    dag = 0
    cor[v] = "cinza"
    for adjacente in listaAdj[v]:
        if cor[adjacente] == "cinza":
            return 1
        if adjacente not in visitados:
            dag = DFS(listaAdj, adjacente, visitados, cor)
    cor[v] = "preto"
    return dag


def verificaDAG(listaAdj):
    visitados = []
    cor = {}
    for i in listaAdj:
        cor[i] = "branco"
    dag = DFS(listaAdj, 0, visitados, cor)
    if dag == 1:
        print("NÃO DAG")
        return str("NÃO DAG")
    print("DAG")
    return str("DAG")