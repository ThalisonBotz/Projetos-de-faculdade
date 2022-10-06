def buscaEmProfundidade(origemChave, destinoChave, nodes):
  pilha = [] 
  visitados = set()

  pilha.append(origemChave)

  while (len(pilha) > 0):
    noCorrenteChave = pilha.pop()

    noCorrente = next((sub for sub in nodes if sub.get(noCorrenteChave)), None) 

    if (noCorrenteChave == destinoChave):
      print('Cidade encontrada!')
      print(destinoChave) 
      return True

    if (noCorrenteChave not in visitados):
      visitados.add(noCorrenteChave)


      for vizinho in  noCorrente[noCorrenteChave]:
        keys = vizinho.keys()
        vizinhoChave = list(keys)[0]
        if (vizinhoChave not in visitados):
          pilha.append(vizinhoChave)
  
  print('Cidade Inexistente !')
  return False