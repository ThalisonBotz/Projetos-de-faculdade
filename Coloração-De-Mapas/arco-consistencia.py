import networkx as nx
#Importação do pacote NetworkX, ultilizado na manipulação de grafos.
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

variaveis = [i for i in G.nodes]
#Criando variaveis de acordo com os nós.
restricoes = [list(G.adj[i]) for i in range(vertices)]
#Definindo as restrições de funcionamento do codigo, o mesmo so funciona se existir elementos nos vertices.
dominios = [["vermelho", "verde", "azul"] for i in range(vertices)]
#Cores que podem ser atribuidas.
atribuicoes = { }
arcos = []
#Definição de arcos

#Preenche a fila com os arcos
def preencher():
    for i in variaveis:
        varIndice = variaveis.index(i)
        for arco in restricoes[varIndice]:
            arcos.append([i, arco])

#AC3
def AC3():
    preencher()
    while arcos:
        varArcos = arcos.pop(0)
        if revisar(varArcos[0], varArcos[1]):

            indiceDominio = variaveis.index(varArcos[0])
            if len(dominios[indiceDominio]) == 0:
                return False

            visinhos = list(restricoes[indiceDominio])
            visinhos.remove(varArcos[1])

            for Xk in visinhos:
                arcos.append([Xk, varArcos[0]])
    print("\nVizinhos:")
    for i in range(vertices):
        print(i, "-", restricoes[i] )
    print("\nResultado:", atribuicoes, "\n")

    return True


#Revisa os nós
def revisar(Xi, Xj):
    revisado = False

    indiceRevisar = variaveis.index(Xi)

    for x in dominios[indiceRevisar]:

        if Xj not in restricoes[indiceRevisar]:
            break

        if Xj not in atribuicoes:
            continue

        if x in atribuicoes[Xj]:
            dominios[indiceRevisar].remove(x) 
            revisado = True

    if not revisado and len(dominios[indiceRevisar]) > 0:
        atribuicoes[Xi] = dominios[indiceRevisar][0]

    return revisado

AC3()
#Executa a função de coloração por arco consistencia.