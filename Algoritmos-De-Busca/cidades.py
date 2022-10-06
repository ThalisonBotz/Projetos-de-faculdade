
# Estrutura de uma cidade
# {                                   {        
#   'Arad': [                           Cidade : [     
#     {'Zerind': 75},                     {CidadeVizinha: Distância entre Cidade e CidadeVizinha}         
#     {'Sibíu': 75},          --->      ]
#     {'Timisoara': 75}               }
#   ]
# }
import json

arquivoCidades = open('cidades.json', 'r')
cidades = json.load(arquivoCidades)
arquivoCidades.close()

arquivoheuristicaGuanambiPotiragua = open('heuristicaGuanambiPotiragua.json', 'r')
heuristicaGuanambiPotiragua = json.load(arquivoheuristicaGuanambiPotiragua)
arquivoheuristicaGuanambiPotiragua.close()


