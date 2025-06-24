from core.problem import Problem
from core.node import Node

def depthFirstSearch(search_tree,problem):
    node = search_tree.getStartNode(problem)
    stack = []
    marked = []
    stack.append(node)

    while len(stack) > 0:
        node = stack.pop()

        if not marked[node]:
            if problem.goal_state(node.state) == True:
                print("Solução encontrada no Node = ", node.state)
                print("Sequência de ações : ", search_tree.getActionSequence(node))
                return search_tree.getActionSequence(node)
            marked.append(node)
            for child in node.expand:
                if not marked[child]:
                    stack.append(child)