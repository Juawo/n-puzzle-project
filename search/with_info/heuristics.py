def misplaced_tiles(state, goal_state):
    misplaceds = 0
    for i in range(len(state)):
        if(state[i] == goal_state[i]):
            continue
        misplaceds += 1
    return misplaceds
            

def manhattan_distance(state, goal_state, board_size):
    distance = 0
    
    # Percorrendo o estado atual
    for value in state:
        if value == 0:
            continue
        
        # Capturando index do valor atual, no estado atual e no estado objetivo
        index_current = state.index(value)
        index_goal = goal_state.index(value)
        
        # Calculando a linha do valor atual no estado atual e no estado objetivo
        row_state = index_current // board_size
        row_goal_state = index_goal // board_size
        
        # Calculando a coluna do valor atual no estado atual e no estado objetivo
        collumn_state = index_current % board_size
        collumn_goal_state = index_goal % board_size

        # Aplicando a fórmula da distância Manhattan
        distance += abs(row_state - row_goal_state) + abs(collumn_state - collumn_goal_state)

    return distance
