from core.problem import Problem
from core.node import Node
from search.no_info.dfs import depthFirstSearch
from search.no_info.bfs import breadthFirstSearch
from search.with_info import heuristics

estado_inicial = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

estado_objetivo = (
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=3)
print(heuristics.manhattan_distance(puzzle.initial_state, puzzle.goal_state, puzzle.board_size))

# print(puzzle.isGoalState(estado_inicial))

# actionSequence = depthFirstSearch(puzzle)
# actionSequence1 = breadthFirstSearch(puzzle)