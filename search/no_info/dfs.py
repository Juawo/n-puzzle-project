from core.problem import Problem
from core.node import Node
from core import search_tree

def depthFirstSearch(problem):
    node = search_tree.getStartNode(problem)
    stack = []
    marked = set()
    stack.append(node)

    passos = 0
    while len(stack) > 0:
        node = stack.pop()
        print(node.depth)
        if node.state not in marked:
            if problem.isGoalState(node.state) == True:
                print("Sequência de ações : ", search_tree.getActionSequence(node))
                return search_tree.getActionSequence(node)
            marked.add(node.state)
            for child in node.expand(problem):
                if child.state not in marked:
                    stack.append(child)