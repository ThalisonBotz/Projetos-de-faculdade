import networkx as nx
# Importação do pacote NetworkX, ultilizado na manipulação de grafos. 
G = nx.Graph()
# Criação de um objeto do tipo gráfico.
with open("arquivo.txt") as arquivo:
#Abrindo o arquivo txt que contem o grafo.
    arq = arquivo.readlines()[0] 
    linha = arq.split()
    vertices = int(linha[0])
    arestas = int(linha[1])
    #Definindo as linhas, arestas e vertices do arquivo aberto.
for i in range(vertices):
    G.add_node(i)
    #Criando o primeiro nó.
for i in range(1, arestas+1):
    with open("arquivo.txt") as arquivo:
        arq = arquivo.readlines()[i]
        linha = arq.split()
        v = int(linha[0])
        u = int(linha[1])
        G.add_edge(v, u)


restricoes = [list(G.adj[i]) for i in range(vertices)]
#Definindo as restrições de funcionamento do codigo, o mesmo so funciona se existir elementos nos vertices.
dominios = ["","vermelho", "verde", "azul"]
#Cores que podem ser atribuidas.
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
    print("\Resultado:", resultado, "\n")
    
colorirGrafo()
#Executando a função.