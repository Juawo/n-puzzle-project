from core import search_tree
from . import heuristics
from utils.results import save_results
import heapq

def aStarSearch(problem, heuristic_type="misplaced_tiles"):
    start_node = search_tree.getStartNode(problem)
    expand_nodes = 0

    if heuristic_type == "misplaced_tiles":
        start_node.heuristic = heuristics.misplaced_tiles(problem.initial_state, problem.goal_state)
    else :
        start_node.heuristic = heuristics.manhattan_distance(problem.initial_state, problem.goal_state)
    
    priority_queue = []
    heapq.heappush(priority_queue, ((start_node.heuristic + start_node.path_cost), start_node))
    # print(f" Raiz => State = {start_node.state} || Path Cost = {start_node.path_cost} || Heuristic = {start_node.heuristic} \n f(n) = {start_node.path_cost + start_node.heuristic}")
    
    visited_nodes = set()

    while priority_queue :
        _, node = heapq.heappop(priority_queue)
        visited_nodes.add(node)

        print(f" State = {node.state} || Path Cost = {node.path_cost} || Heuristic = {node.heuristic} \n f(n) = {node.path_cost + node.heuristic}\n")
        
        # print(f"Path Cost = {node.path_cost} || Heuristic = {node.heuristic} || f(n) = {start_node.path_cost + node.heuristic}")

        if problem.isGoalState(node.state):
            return search_tree.getActionSequence(node)
        
        for sucessor in node.expand(problem):
            if heuristic_type == "misplaced_tiles":
                sucessor.heuristic = heuristics.misplaced_tiles(sucessor.state, problem.goal_state)
            else:
                sucessor.heuristic = heuristics.manhattan_distance(sucessor.state, problem.goal_state)
            
            print(f"    Sucessor do Node ({node.state})\n    State = {sucessor.state} || Path Cost = {sucessor.path_cost} || Heuristic = {sucessor.heuristic} \n f(n) = {sucessor.path_cost + sucessor.heuristic}\n")

            if sucessor not in priority_queue and sucessor not in visited_nodes:
                heapq.heappush(priority_queue, ((sucessor.path_cost + sucessor.heuristic), sucessor))
        
        expand_nodes +=1

    return 'failure'
            



    return