# Definição de Node -> Slide Slides 02 - Agentes e Problemas de Busca -> pág 67

class Node:

    # Construturo da classe
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
    
    # Compara o menor custo de caminho entre dois Nós
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    #   Função para expandir um nó, ou seja, ver quais filhos ele possui, salvando os resultados das ações possíveis nele 
    def expand(self, problem):
        # print("[DEBUG] Chamando actions em Node Expand: ", problem.actions(self.state))
        children = []
        for action in problem.actions(self.state):
            new_state = problem.result(self.state, action)
            cost = problem.pathCost(self.path_cost, self.state, action, new_state)
            child = Node(
                state=new_state,
                parent=self,
                action=action,
                path_cost=cost,
                depth=self.depth + 1
            )
            children.append(child)
        # print(children)
        return children

    #   Função para encontrar qual o caminho de ações para aquele Nó/Estado 
    def solution(self):
        actions = []
        node = self
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        return list(reversed(actions))