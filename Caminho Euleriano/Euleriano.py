def caminhoEuleriano(matriz):
    n = len(matriz[0])
    total = 0
    i = 0
    while total <= 2 and (i<n):
        grau = 0
        for j in range(0, n):
            grau += matriz[i][j]
        if grau % 2 != 0:
            total = total+1
        i = i+1
    if total > 2:
        print(False)
        return False
    else:
        print(True)
        return True