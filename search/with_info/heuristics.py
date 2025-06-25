def misplaced_tiles(state, goal_state):
    misplaceds = 0
    for i in range(len(state)):
        if(state[i] == goal_state[i]):
            continue
        misplaceds += 1
    return misplaceds
            

def manhattan_distance(state, goal_state, board_size):
    return