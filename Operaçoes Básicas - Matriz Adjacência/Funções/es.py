import numpy as np

def entrada(instancia):
    caminho = 'C:/Users/tiago/OneDrive/Documentos/Tiago/Ciência da Computação/3º Período/Algoritmos em Grafos/AT2/Instancias/' + instancia +'.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f,"int")
    return data

def saida(instancia, dim):
    print("Nome Instancia = %s" % instancia)
    print("Quantidade de linhas = %d, quantidade de colunas = %d" % (dim[0],dim[1]))
    with open('C:/Users/tiago/OneDrive/Documentos/Tiago/Ciência da Computação/3º Período/Algoritmos em Grafos/AT1/Resultados/resultado.txt','w') as file:
        file.write('%s %d %d\n' % (instancia,dim[0],dim[1]))