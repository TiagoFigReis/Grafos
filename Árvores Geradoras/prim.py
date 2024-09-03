
def prim(matriz):
    v = 0
    S = [0]
    N = [i for i in range(len(matriz)) if i != v]
    T = []
    while len(T) < len(matriz) - 1:
        menor_peso = float('inf')
        for i in S:
            for j in N:
                if matriz[i][j] != 0 and matriz[i][j] < menor_peso:
                    menor_peso = matriz[i][j]
                    menor_v = i
                    menor_u = j
        S.append(menor_u)
        N.remove(menor_u)
        T.append((menor_v, menor_u))

    soma = 0
    for aresta in T:
        soma += matriz[aresta[0]][aresta[1]]
    print(T, soma)


prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9,
     0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])
