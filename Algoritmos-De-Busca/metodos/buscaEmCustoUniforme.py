import math

# Coloca todos os nós com uma distância infinita e retorna um dicionário com a cidade sendo a chave e a distância o valor
# Param:
#   nos -> conjunto de nós da arvóre ou grafo
# Return: 
# [(Cidade, DistânciaInfinita),...]

def colocaTodosOsNosComDistanciaInfinita(nos):
  distancia = {}
  for no in nos:
    keys = no.keys()
    nodeKey = list(keys)[0]
    distancia[nodeKey] = math.inf
  
  return distancia

# Retorna o Nó com a menor distância dentro da fila
def pegaNoComMenorDistancia(fila, distancia):
  noComMenorDistancia = None
  for no in fila: 
      if noComMenorDistancia == None:
          noComMenorDistancia = no
      elif distancia[no] < distancia[noComMenorDistancia]:
          noComMenorDistancia = no

  return noComMenorDistancia

#distancia de saida ou origem 
def expansionProcess(origemChave, nos):
  visitados = set()  # Conjunto dos nós visitados
  fila = []    # Fila
  anteriores = {}

  distancia = colocaTodosOsNosComDistanciaInfinita(nos) 

  distancia[origemChave] = 0 # Custo das origens 

  fila.insert(0, origemChave) # Insere a origem na fila 
  visitados.add(origemChave) # Atualiza o nó como visitado
  while (len(fila) != 0):
    noCorrenteChave = pegaNoComMenorDistancia(fila, distancia)  

    fila.remove(noCorrenteChave)
    
    noCorrente = next((sub for sub in nos if sub.get(noCorrenteChave)), None) # Traz dados da Cidades vizinhos e custos 
  
    for vizinho in noCorrente[noCorrenteChave]:
      keys = vizinho.keys()
      vizinhoChave = list(keys)[0] # Nome da cidade
      valorCusto = vizinho[vizinhoChave] # Distância e Custo entre a Cidade selecionada e sua Vizinha

      custo = distancia[noCorrenteChave] + valorCusto
      if (custo < distancia[vizinhoChave]):
        distancia[vizinhoChave] = custo
        anteriores[vizinhoChave] = noCorrenteChave
      
      if (vizinhoChave not in visitados):
         fila.insert(0, vizinhoChave) # entra cidade vizinha na fila
         visitados.add(vizinhoChave) # Atualiza o nó como visitado

  return anteriores, distancia


#informa o custo , caminho minimo encontrado entre as cidades ou mostra que nao localizou
def buscaEmCustoUniforme(origemChave, destinoChave, nos):

  (anteriores, distancia) = expansionProcess(origemChave, nos)

  caminho = []
  noCorrente = destinoChave
  while noCorrente != origemChave:
      if noCorrente not in anteriores:
          print("Caminho não encontrado! As cidade estão correta?")
          return False
      else:
          caminho.insert(0, noCorrente) 
          noCorrente = anteriores[noCorrente]
  caminho.insert(0, origemChave)

  if destinoChave in distancia and distancia[destinoChave] != math.inf:
      print('Custo do caminho mínimo ' + str(distancia[destinoChave]))
      print('Caminho encontrado: ', end='')
      for p in caminho:
        print('-> ' + p, end='')
        print(flush=True)

  return True