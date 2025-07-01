from core.problem import Problem
from core.node import Node
from search.no_info.dfs import depthFirstSearch
from search.no_info.bfs import breadthFirstSearch
from search.no_info.dls import depthLimitedSearch
from search.no_info.ids import iterativeDepthSearch
from search.with_info import heuristics

# Estado inicial simples (0 é o espaço vazio)
estado_inicial =  (3,1,2,
                   0,4,5,
                   6,7,8)
# Estado objetivo (padrão do puzzle 15)
estado_objetivo = (0,1,2,
                   3,4,5,
                   6,7,8)

# # Estado inicial simples (0 é o espaço vazio)
# estado_inicial =  (5,13,14,11,
#                    12,8,2,4,
#                    15,0,9,1,
#                    3,6,7,10)
# # Estado objetivo (padrão do puzzle 15)
# estado_objetivo = (0,1,2,3,
#                    4,5,6,7,
#                    8,9,10,11,
#                    12,13,14,15)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=3)
# dfs = depthFirstSearch(puzzle)
ids = iterativeDepthSearch(puzzle)

# print(heuristics.manhattan_distance(puzzle.initial_state, puzzle.goal_state, puzzle.board_size))


# print(puzzle.isGoalState(estado_inicial))

# actionSequence = depthLimitedSearch(puzzle, 0)
# print("Solução encontrada:", actionSequence)
# actionSequence = depthFirstSearch(puzzle)
# actionSequence1 = breadthFirstSearch(puzzle)