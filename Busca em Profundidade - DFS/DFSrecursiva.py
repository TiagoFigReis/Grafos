def DFS(lista_adjacencia,v,visitados = []):
    if not visitados:
        visitados = []
    DeepFirstSearch(lista_adjacencia,v,visitados)
    print(visitados)
    return visitados

def DeepFirstSearch(lista_adjacencia,v,visitados = []):
    visitados.append(v)
    for i in lista_adjacencia[v]:
        if i not in visitados:
            DeepFirstSearch(lista_adjacencia, i, visitados)
    return visitados
