from core.problem import Problem
from core.node import Node
from core import search_tree

def depthLimitedSearch(problem, limit):
    node = search_tree.getStartNode(problem)
    stack = [node]
    marked = set()
    cutoff = False

    while stack:
        node = stack.pop()
        print(node.depth)
        print(node.state)

        if node in marked:
            continue
        
        marked.add(node.state)

        if problem.isGoalState(node.state):
            print("Sequência de ações:", search_tree.getActionSequence(node))
            return search_tree.getActionSequence(node)

        if node.depth == limit:
            cutoff = True
        else:
            for child in node.expand(problem):
                stack.append(child)

    return 'cutoff' if cutoff else 'failure'
