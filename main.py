from core.problem import Problem
from core.node import Node
from search.dfs import depthFirstSearch

# Estado inicial simples (0 é o espaço vazio)
estado_inicial = (7, 0, 5,
                  2, 6, 4,
                  8, 1, 3)

# Estado objetivo (padrão do puzzle 8)
estado_objetivo = (0, 1, 2,
                   3, 4, 5,
                   6, 7, 8)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=3)

# print(puzzle.isGoalState(estado_inicial))

actionSequence = depthFirstSearch(puzzle)
