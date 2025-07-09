from core.problem import Problem
from core.node import Node
from core import search_tree
from utils.results import save_results
import time


def depthFirstSearch(problem):
    node = search_tree.getStartNode(problem)
    stack = []
    marked = set()
    stack.append(node)
    # Essa variável foi adicionada após o vídeo, para que pudesse ser exibida a árvore gerada
    arvore_busca = []

    expand_nodes = 0
    start_time = time.time()

    while len(stack) > 0:
        node = stack.pop()

        if node.state not in marked:
            if problem.isGoalState(node.state) == True:
                end_time = time.time()
                path = node.solution()
                save_results(algoritmo="DepthFirstSearch", estado_inicial=problem.initial_state,estado_objetivo=problem.goal_state,
                caminho=path,
                profundidade=node.depth,
                nos_expandidos=expand_nodes,
                estados_expandidos=len(marked),
                tempo_exec=end_time - start_time,
                board_size=problem.board_size,
                arvore_gerada=arvore_busca
                )

                return search_tree.getActionSequence(node)
            marked.add(node.state)

            for child in node.expand(problem):
            # Adicionando os node expandidos na arvore de busca gerada
                arvore_busca.append((node.state, child.state, child.action))
                if child.state not in marked:
                    stack.append(child)
            expand_nodes += 1
    print(len(marked))