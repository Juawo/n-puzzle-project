from core.problem import Problem
from core.node import Node
from search.no_info.dfs import depthFirstSearch
from search.no_info.bfs import breadthFirstSearch
from search.no_info.dls import depthLimitedSearch
from search.no_info.ids import iterativeDepthSearch

from search.with_info.greddy import greedySearch
from search.with_info.a_star import aStarSearch

# Estado inicial simples (0 é o espaço vazio)
estado_inicial =  (3,1,2,
                   4,0,5,
                   6,7,8)
# Estado objetivo (padrão do puzzle 15)
estado_objetivo = (0,1,2,
                   3,4,5,
                   6,7,8)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=3)
# dfs = depthFirstSearch(puzzle)
# bfs = breadthFirstSearch(puzzle)
# dls = depthLimitedSearch(puzzle,10)
# ids = iterativeDepthSearch(puzzle)
# greedy = greedySearch(puzzle)
a_star = aStarSearch(puzzle)
print(a_star)
