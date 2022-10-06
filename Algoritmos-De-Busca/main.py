# 1) Busca Primeiro na Largura          DONE
# 2) Busca de Custo Uniforme            DONE
# 3) Busca Primeiro na Profundidade     DONE           


from metodos.buscaEmLargura import buscaEmLargura
from metodos.buscaEmCustoUniforme import buscaEmCustoUniforme
from metodos.buscaEmProfundidade import buscaEmProfundidade
from cidades import cidades, heuristicaGuanambiPotiragua


import sys

algoritmo = sys.argv[1]

origem = 'Guanambi'
destino = 'Potiragua'
if (algoritmo == '1'):
  print('Busca Em Largura\n\n')
  buscaEmLargura(origem, destino, cidades)
elif (algoritmo == '2'):
  print('Busca de Custo Uniforme\n\n')
  buscaEmCustoUniforme(origem, destino, cidades)
elif (algoritmo == '3'):
  print('Busca Em Profundidade\n\n')
  buscaEmProfundidade(origem, destino, cidades)
else:
  print("Algoritmo não encontrado")
  print('Escolha um número entre 1 a 3')
  print('Busca em Largura: 1; Busca de Custo Uniforme: 2; Busca em Profundidade: 3')

