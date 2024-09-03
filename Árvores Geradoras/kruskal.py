class Conjunto():
    def __init__(self, N):
        # lista de raizes, guarda a raiz de cada elemento do conjunto, inicialmente cada elemento é sua própria raiz,
        # ou seja, cada elemento inicialmente é um conjunto separado
        # conforme vai ocorrendo a união dos conjuntos separados (união de componentes conexas), a raiz de um elemento passa a ser outro elemento
        # logo ao consultar a raiz de dois elementos, se elas forem iguais, significa que pertencem ao mesmo conjunto (componente conexa)
        # o elemento a se tornar raiz depende do valor de seu posto (altura da arvore a qual esse elemento é raiz), inicialmente o posto de cada elemento é 0
        # pois ele não tem ligação com outro elemento. Para decidir na uniao de dois conjuntos quem vai se tornar a raiz do novo conjunto, é utilizado o valor do posto
        # o elemento de menor posto, juntamente dos elementos associados a eles, se tornarão parte do conjunto do elemento de maior posto e, o conjunto do elemento
        # de menor é descartado. Se dois postos forem iguais, um dos elementos é escolhido arbitrariamente e entao é aumentado seu posto em uma unidade,
        # essa decisao dependera da implementação do algoritmo
        self.__raizes = [i for i in N]
        # lista de posto guarda o posto de cada elemento
        self.__posto = [0]*len(N)

    # retorna a raiz de um conjunto
    def findset(self, u):
        if self.__raizes[u] != u:
            # Realiza a compressão de caminho fazendo cada nó de um conjunto (componente conexa) apontar diretamente para a raiz(elemento de maior posto na componente)
            self.__raizes[u] = self.findset(self.__raizes[u])
        return self.__raizes[u]

    # faz a união de dois conjuntos se eles ja não pertencem ao mesmo conjunto
    def union(self, u, v):
        raiz_u = self.findset(u)
        raiz_v = self.findset(v)

        # se eles tem a mesma raiz pertencem ao mesmo conjunto
        if raiz_u == raiz_v:
            return

        # une duas componentes conexas do grafo, o elemento a se tornar raiz vai ser aquele de maior posto
        if self.__posto[raiz_u] > self.__posto[raiz_v]:
            self.__raizes[raiz_v] = raiz_u
        else:
            self.__raizes[raiz_u] = raiz_v
            if self.__posto[raiz_u] == self.__posto[raiz_v]:
                self.__posto[raiz_v] += 1

# Essa estrutura de dados evita ciclos pois verifica se dois vertices (os quais apresentam uma aresta entre si) ja estao na mesma componente conexa
# (findset(v) = findset(u)). Se isso ocorre, a ligação entre eles acarretara na formação um ciclo, senao é feito a uniao entre eles. Logo, ao final
# do algoritmo de kruskal serao selecionadas as arestas de menor peso (visto que o conjunto H a ser analisado apresenta todas as arestas do grafo
# ordenadas com base em seu peso) e que garantem que cada vertice da arvore estao conectados


def kruskal(matriz):
    conjunto = Conjunto([i for i in range(0, len(matriz))])
    H = []
    T = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0 and (j, i, matriz[j][i]) not in H:
                H.append((matriz[i][j],i, j))

    H.sort()

    while len(T) < len(matriz) - 1:
        arestas = H.pop(0)
        if conjunto.findset(arestas[1]) != conjunto.findset(arestas[2]):
            T.append((arestas[1], arestas[2]))
            conjunto.union(arestas[1], arestas[2])

    soma = 0
    for aresta in T:
        soma += matriz[aresta[0]][aresta[1]]

    print(T, soma)


kruskal([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9,
        0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])
