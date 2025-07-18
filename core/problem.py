# Definição de Problema de Busca -> Slide Slides 02 - Agentes e Problemas de Busca -> pág 25

class Problem:
    
    # Construtor da classe
    def __init__(self, initial_state, goal_state, board_size):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.board_size = board_size
    
    # Função que retorna as ações possivéis no estado atual
    def actions(self, state):
        
        index = state.index(0)
        row = index // self.board_size
        collumn = index % self.board_size
        actions = []
        
        if row < self.board_size - 1 : actions.append("baixo")
        if collumn > 0 : actions.append("esquerda")
        if collumn < self.board_size - 1 : actions.append("direita")
        if row > 0 : actions.append("cima")
        # print(actions)
        return actions

    # Função que retorna o resultado de aplicar determinada ação em determinado estado
    def result(self, state, action):
        new_state = list(state)
        index = new_state.index(0)
        row = index // self.board_size
        collumn = index % self.board_size
        swap_index = 0

        if action == "cima":
            swap_index = (row - 1) * self.board_size + collumn
        elif action == "baixo":
            swap_index = (row + 1) * self.board_size + collumn
        elif action == "esquerda":
            swap_index =  self.board_size * row + (collumn - 1)
        elif action == "direita":
            swap_index = self.board_size * row + (collumn + 1) 
        
        temp = new_state[index]
        new_state[index] = new_state[swap_index]
        # print(new_state[index])

        new_state[swap_index] = temp
        # print(new_state[swap_index])

        return tuple(new_state)
    
    # Função para verificar se o estado atual é o estado objetivo
    def isGoalState(self, state):
        return self.goal_state == state

    # Função para retornar o custo do caminho, custo do caminho até agora + 1
    def pathCost(self, cost_so_far, state1, action, state2):
        return cost_so_far + 1
    