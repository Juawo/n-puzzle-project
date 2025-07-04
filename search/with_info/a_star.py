from core import search_tree
from . import heuristics
import heapq
from utils.results import save_results
import time

def aStarSearch(problem, heuristic_type="misplaced_tiles"):
    start_node = search_tree.getStartNode(problem)
    expand_nodes = 0
    start_time = time.time()

    if heuristic_type == "misplaced_tiles":
        start_node.heuristic = heuristics.misplaced_tiles(problem.initial_state, problem.goal_state)
    else :
        start_node.heuristic = heuristics.manhattan_distance(problem.initial_state, problem.goal_state)
    
    priority_queue = []
    heapq.heappush(priority_queue, ((start_node.heuristic + start_node.path_cost), start_node))
    
    visited_nodes = set()

    while priority_queue :
        _, node = heapq.heappop(priority_queue)
        visited_nodes.add(node.state)

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
                heuristc=heuristic_type
            )

            return search_tree.getActionSequence(node)
        
        for sucessor in node.expand(problem):
            if heuristic_type == "misplaced_tiles":
                sucessor.heuristic = heuristics.misplaced_tiles(sucessor.state, problem.goal_state)
            else:
                sucessor.heuristic = heuristics.manhattan_distance(sucessor.state, problem.goal_state)
            
            print(f"    Sucessor do Node ({node.state})\n    State = {sucessor.state} || Path Cost = {sucessor.path_cost} || Heuristic = {sucessor.heuristic} \n f(n) = {sucessor.path_cost + sucessor.heuristic}\n")

            if sucessor.state not in visited_nodes:
                heapq.heappush(priority_queue, ((sucessor.path_cost + sucessor.heuristic), sucessor))
        
        expand_nodes +=1

    return 'failure'