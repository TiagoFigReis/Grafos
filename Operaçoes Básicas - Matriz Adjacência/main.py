from Funções import (grafos as g, es)

instancia = input("Digite a instancia:")
matriz = es.entrada(instancia)
print(matriz)
print(g.verificaAdjacencia(matriz, 1, 1))
print(g.calcDensidade(matriz))
print(g.tipoGrafo(matriz))
print(g.insereVertice(matriz))
print(g.insereAresta(matriz,3,2))
print(g.removeAresta(matriz,0,1))
print(g.removeVertice(matriz,4))