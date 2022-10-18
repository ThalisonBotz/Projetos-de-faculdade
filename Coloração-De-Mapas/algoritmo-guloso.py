import networkx as nx

G = nx.Graph()

with open("arquivo.txt") as arquivo:
    arq = arquivo.readlines()[0] 
    linha = arq.split()
    vertices = int(linha[0])
    arestas = int(linha[1])

for i in range(vertices):
    G.add_node(i)

for i in range(1, arestas+1):
    with open("arquivo.txt") as arquivo:
        arq = arquivo.readlines()[i]
        linha = arq.split()
        v = int(linha[0])
        u = int(linha[1])
        G.add_edge(v, u)


restricoes = [list(G.adj[i]) for i in range(vertices)]
dominios = ["","vermelho", "verde", "azul"]
resultado = { }

def colorirGrafo():
    for u in range(vertices):
        atribuido = set([resultado.get(i) for i in restricoes[u] if i in resultado])
        cor = 1
        for c in atribuido:
            if cor != c:
                break
            cor = cor + 1
        resultado[u] = cor
 
    for i in range(vertices):
        resultado[i] = dominios[resultado[i]]
    
    print("\nVizinhos:")
    for i in range(vertices):
        print(i, "-", restricoes[i] )
    print("\nSolução:", resultado, "\n")
    
colorirGrafo()