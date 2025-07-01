from core.problem import Problem
from core.node import Node
from core import search_tree
from utils.results import save_results
import time

def depthLimitedSearch(problem, limit):
    node = search_tree.getStartNode(problem)
    stack = [node]
    marked = set()
    cutoff = False
    start_time = time.time()
    expand_node = 0

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
            
            save_results(
                algoritmo="DLS",
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=path,
                profundidade=node.depth,
                nos_expandidos=expand_node,
                estados_expandidos=marked,
                tempo_exec=end_time - start_time
            )
            print("Sequência de ações : ", search_tree.getActionSequence(node))
            return search_tree.getActionSequence(node)

        if node.depth == limit:
            cutoff = True
            end_time = time.time()
            path = search_tree.getActionSequence(node)
            
            save_results(
                algoritmo="DLS",
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=path,
                profundidade=node.depth,
                nos_expandidos=expand_node,
                estados_expandidos=marked,
                tempo_exec=end_time - start_time
            )
            print("Limite atingido.")

        if node.depth < limit:
            expand_node += 1
            for child in node.expand(problem):
                stack.append(child)
        else:
            return cutoff

