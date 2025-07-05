from collections import deque
from core.problem import Problem
from core.node import Node
from core import search_tree
from utils.results import save_results
import time

# CONSTRUÇÃO DAS FUNÇÕES DE BUSCA SEM INFORMAÇÃO (BUSCA EM LARGURA):
def breadthFirstSearch(problem):
    start_node = search_tree.getStartNode(problem)
    fronteira = deque()
    fronteira.append(start_node)
    explorados = set()

    start_time = time.time()
    expand_node = 0

    while fronteira:
        node = fronteira.popleft()
        state = tuple(node.state) 

        if state in explorados:
            continue

        explorados.add(state)

        if problem.isGoalState(node.state) == True:
            end_time = time.time()
            path = search_tree.getActionSequence(node)
            save_results(
                algoritmo="BreadthFirstSearch",
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=path,
                profundidade=node.depth,
                nos_expandidos=expand_node,
                estados_expandidos=len(explorados),
                tempo_exec=end_time - start_time,
                board_size=problem.board_size
            )
            
            print("Sequência de ações : ", search_tree.getActionSequence(node))
            print(len(explorados))
            return search_tree.getActionSequence(node)

        expand_node += 1

        for child in node.expand(problem):
            if tuple(child.state) not in explorados:
                fronteira.append(child)

    return []