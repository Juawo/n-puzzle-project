from core.node import Node

# Função que retorna o nó raiz do problema
def getStartNode(problem):
    return Node(problem.intial_state)

# Função que gera um filho do nó atual
def getChildNode(problem, parent_node, action):
    new_state = problem.result(parent_node, action)
    new_cost = problem.path_cost(parent_node.path_cost, parent_node.state, action, new_state)
    return Node(
        state=new_state,
        parent=parent_node,
        action=action,
        path_cost=new_cost,
        depth=parent_node.depth + 1
    )

# Função que acessa e retorna o caminho de ações para chegar em determinado Nó
def getActionSequence(node):
    return node.solution()