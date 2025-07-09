from core.problem import Problem
from core.node import Node
from core import search_tree
from utils.results import save_results
import time

def depthLimitedSearch(problem, limit, ids=False):
    node = search_tree.getStartNode(problem)
    stack = [node]
    marked = set()
    cutoff = False
    start_time = time.time()
    expand_node = 0
    arvore_busca = []

    while stack:
        node = stack.pop()
        print(node.depth)
        print(node.state)

        if node in marked:
            continue
        
        marked.add(node.state)

        if problem.isGoalState(node.state):
            end_time = time.time()
            path = search_tree.getActionSequence(node)
            algorithm = ""
            if(ids):
                algorithm = "IDS"
            else:
                algorithm = "DLS"
                
            save_results(
                algoritmo=algorithm,
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=path,
                profundidade=node.depth,
                nos_expandidos=expand_node,
                estados_expandidos=len(marked),
                tempo_exec=end_time - start_time,
                board_size=problem.board_size,
                arvore_gerada=arvore_busca
            )
            print("Sequência de ações:", search_tree.getActionSequence(node))
            return search_tree.getActionSequence(node)

        if node.depth == limit:
            cutoff = True
        else:
            for child in node.expand(problem):
                arvore_busca.append((node.state, child.state, child.action))
                stack.append(child)
            expand_node += 1

    return 'cutoff' if cutoff else 'failure'
