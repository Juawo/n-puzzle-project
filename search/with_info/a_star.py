from core import search_tree
from . import heuristics
import heapq
from utils.results import save_results
import time

def aStarSearch(problem, heuristic_type="manhattan_distance"):
    start_node = search_tree.getStartNode(problem)
    expand_nodes = 0
    start_time = time.time()
    # Essa variável foi adicionada após o vídeo, para que pudesse ser exibida a árvore gerada
    arvore_busca = []

    if heuristic_type == "misplaced_tiles":
        start_node.heuristic = heuristics.misplaced_tiles(problem.initial_state, problem.goal_state)
    else :
        start_node.heuristic = heuristics.manhattan_distance(problem.initial_state, problem.goal_state, problem.board_size)
    
    priority_queue = []
    heapq.heappush(priority_queue, ((start_node.heuristic + start_node.path_cost), start_node))
    
    visited_nodes = set()

    while priority_queue :
        _, node = heapq.heappop(priority_queue)

        print(f" State = {node.state} || Path Cost = {node.path_cost} || Heuristic = {node.heuristic} \n f(n) = {node.path_cost + node.heuristic}\n")

        if problem.isGoalState(node.state):
            end_time = time.time()

            save_results(
                algoritmo="A*",
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=search_tree.getActionSequence(node),
                profundidade=node.depth,
                nos_expandidos=expand_nodes,
                estados_expandidos=len(visited_nodes),
                tempo_exec=end_time - start_time,
                heuristic=heuristic_type,
                board_size=problem.board_size,
                arvore_gerada=arvore_busca
            )

            return search_tree.getActionSequence(node)
        
        visited_nodes.add(node.state)
        
        for sucessor in node.expand(problem):
            # Adicionando os node expandidos na arvore de busca gerada
            arvore_busca.append((node.state, sucessor.state, sucessor.action))
            if heuristic_type == "misplaced_tiles":
                sucessor.heuristic = heuristics.misplaced_tiles(sucessor.state, problem.goal_state)
            else:
                sucessor.heuristic = heuristics.manhattan_distance(sucessor.state, problem.goal_state, problem.board_size)
            
            print(f"    Sucessor do Node ({node.state})\n    State = {sucessor.state} || Path Cost = {sucessor.path_cost} || Heuristic = {sucessor.heuristic} \n f(n) = {sucessor.path_cost + sucessor.heuristic}\n")

            if sucessor.state not in visited_nodes:
                heapq.heappush(priority_queue, ((sucessor.path_cost + sucessor.heuristic), sucessor))
        
        expand_nodes +=1

    return 'failure'