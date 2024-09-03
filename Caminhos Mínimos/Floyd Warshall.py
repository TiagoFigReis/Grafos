import numpy as np
def floydWarshall(matriz):
    n = len(matriz)
    D = matriz
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] == -1:
                D[i][j] = float('inf')
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if D[i][j] < (D[i][k] + D[k][j]):
                    D[i][j] = D[i][j]
                else:
                    D[i][j] = D[i][k] + D[k][j]
    return D

a = floydWarshall([[0, 3, 8, -1, -4],[-1, 0, -1, 1, 7],[-1, 4, 0, -1, -1],[2, -1, -5, 0, -1],[-1, -1, -1, 6, 0]])
print(a)