import numpy as np
def warshall(matriz):
    n = len(matriz[0])
    r = matriz
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if(r[i][j] == 1 or (r[i][k]==1 and r[k][j]==1)):
                    r[i][j] = 1
                else: 
                    r[i][j] = r[i][j]
    print(np.array(r))
    return r