from core.problem import Problem
from core.node import Node
from search.no_info.dfs import depthFirstSearch
from search.no_info.bfs import breadthFirstSearch

# Estado inicial simples (0 é o espaço vazio)
estado_inicial = (1, 2, 6, 3,
                   4, 5, 0, 7, 
                   8, 9, 10, 11,
                   12, 13, 14, 15)

# Estado objetivo (padrão do puzzle 8)
estado_objetivo = (0, 1, 2, 3,
                   4, 5, 6, 7, 
                   8, 9, 10, 11,
                   12, 13, 14, 15)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=4)

# print(puzzle.isGoalState(estado_inicial))

actionSequence = depthFirstSearch(puzzle)
actionSequence1 = breadthFirstSearch(puzzle)
