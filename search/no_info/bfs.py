from collections import deque
from core.problem import Problem
from core.node import Node
from core import search_tree

# CONSTRUÇÃO DAS FUNÇÕES DE BUSCA SEM INFORMAÇÃO (BUSCA EM LARGURA):
def breadthFirstSearch(problem):
    start_node = search_tree.getStartNode(problem)
    fronteira = deque()
    fronteira.append(start_node)
    explorados = set()

    while fronteira:
        node = fronteira.popleft()
        state = tuple(node.state) 

        if state in explorados:
            continue

        explorados.add(state)

        if problem.isGoalState(node.state) == True:
            print("Sequência de ações : ", search_tree.getActionSequence(node))
            return search_tree.getActionSequence(node)

        for child in node.expand(problem):
            if tuple(child.state) not in explorados:
                fronteira.append(child)

    return []