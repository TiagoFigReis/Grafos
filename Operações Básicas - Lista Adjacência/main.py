from Funções import funcoes as f

instancia = input("Digite a instancia: ")
matriz = f.entrada(instancia)
print(matriz)
lst = f.criaListaAdjacencias(matriz)
print(lst)
print(f.tipoGrafoLista(lst))
print(f.calcDensidade(lst))
print(f.insereAresta(lst,1,2))
print(f.removeArestaLista(lst,1,2))
print(f.removeVerticeLista(lst,2))
print(f.verificaAdjacenciaLista(lst,3,2))
