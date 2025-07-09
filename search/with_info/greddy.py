from core import search_tree
from . import heuristics
from utils.results import save_results
import heapq
import time


def greedySearch(problem, heuristic_type="manhattan_distance"): 

    start_node = search_tree.getStartNode(problem)
    expand_nodes = 0
    start_time = time.time()
    arvore_busca = []

    if heuristic_type == "misplaced_tiles":
        start_node.heuristic = heuristics.misplaced_tiles(problem.initial_state, problem.goal_state)
    else:
        start_node.heuristic = heuristics.manhattan_distance(problem.initial_state, problem.goal_state, problem.board_size)

    open_list = []
    heapq.heappush(open_list, (start_node.heuristic, start_node))

    closed = set()

    while open_list:
        _, node = heapq.heappop(open_list)

        if problem.isGoalState(node.state):
            end_time = time.time()
            save_results(
                algoritmo="GreedySearch",
                estado_inicial=problem.initial_state,
                estado_objetivo=problem.goal_state,
                caminho=search_tree.getActionSequence(node),
                profundidade=node.depth,
                nos_expandidos=expand_nodes,
                estados_expandidos=len(closed),
                tempo_exec=end_time - start_time,
                arvore_gerada=arvore_busca,
                heuristic=heuristic_type,
                board_size=problem.board_size
            )
            return search_tree.getActionSequence(node)
        
        closed.add(node.state)

        for sucessor in node.expand(problem) :
            arvore_busca.append((node.state, sucessor.state, sucessor.action))
            if heuristic_type == "misplaced_tiles" :
                sucessor.heuristic = heuristics.misplaced_tiles(sucessor.state, problem.goal_state)
            else :
                sucessor.heuristic = heuristics.manhattan_distance(sucessor.state, problem.goal_state, problem.board_size)
            
            if sucessor.state not in closed :
               heapq.heappush(open_list, (sucessor.heuristic, sucessor)) 
            
            print(f"    Sucessor do Node ({node.state})\n    State = {sucessor.state} || Heuristic = {sucessor.heuristic} \n f(n) = {sucessor.heuristic}\n")

        expand_nodes += 1

    return "Failure"