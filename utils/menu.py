from core.problem import Problem
from core.node import Node
from search.no_info.dfs import depthFirstSearch
from search.no_info.bfs import breadthFirstSearch
from search.no_info.dls import depthLimitedSearch
from search.no_info.ids import iterativeDepthSearch
from search.with_info.greddy import greedySearch
from search.with_info.a_star import aStarSearch
from .load_puzzles import load_puzzles
import time
import os
import sys
import itertools


def init_menu():
    loop = True
    user_input = None
    data_puzzles = load_puzzles("./utils/puzzles.json")
    while loop:
        display_menu_options();
        user_input = input("Select an option:")

        match user_input:
            case "1":
                result = select_option(3, data_puzzles)
                if result == "continue":
                    continue
                if result == False:
                    loop = False
            case "2":
                result = select_option(4, data_puzzles)
                if result == "continue":
                    continue
                if result == False:
                    loop = False
            case "3":
                result = select_option(5, data_puzzles)
                if result == "continue":
                    continue
                if result == False:
                    loop = False
            case "0":
                print("Exiting...")
                time.sleep(1)
                loop = False
            case _:
                print("Invalid option. Please try again.")
    

def select_option(board_size, data_puzzles):
    puzzle_data = data_puzzles[f"{board_size}x{board_size}"]
    initial_state = tuple(puzzle_data["initial_state"])
    goal_state = tuple(puzzle_data["goal_state"])
    puzzle = Problem(initial_state, goal_state, board_size)
    display_execution_options(board_size)
    user_input = input("Select an option: ")
    pause_clean(1)
    match user_input:
        case "1":
           execute_all_search(board_size, puzzle)
        case "2":
            display_searchs_name(board_size)
            user_input = input("Select an option: ")
            swithc_searchs(board_size, user_input, puzzle)
        case "3":
            return 'continue'
        case "0":
            return False
        case _ :
            print("Invalid option. Please try again.")


def display_menu_options():
    pause_clean(0.2)
    print("------ N-Puzzle Project - Solve 3x3, 4x4, 5x5 with Search Algorithms ------")
    print("Select puzzle board size: ")
    print("  1 - 3x3 Puzzle         <- All algorithms can use")
    print("  2 - 4x4 Puzzle         <- All algorithms can use")
    print("  3 - 5x5 Puzzle         <- Only informated algorithms can use")
    print("  0 - Exit")

def display_execution_options(board_size):
    if(board_size < 5):
        print("You can use all algotithms in this puzzle board size!")
        pause_clean(2)

        print("------ N-Puzzle Project - Solve 3x3, 4x4, 5x5 with Search Algorithms ------")
        print(f"Select an executation type for solve {board_size}x{board_size}: ")
        print("  1 - All algorithms")
        print("     [BFS, DFS, IDS, Greedy Search, A*]")
        print("  2 - Select one algorithm")
        print("     [BFS, DFS, IDS, Greedy Search, A*]")
        print("  3 - Back")
        print("  0 - Exit")
        
    else :
        print("You can use only informated algotithms in this puzzle board size!")
        pause_clean(2)

        print("------ N-Puzzle Project - Solve 3x3, 4x4, 5x5 with Search Algorithms ------")
        print(f"Select an executation type for solve {board_size}x{board_size}: ")
        print("  1 - All algorithms")
        print("     [Greedy Search, A*]")
        print("  2 - Select one algorithm")
        print("     [Greedy Search, A*]")
        print("  3 - Back")
        print("  0 - Exit")

def display_heuristic_options():
    print("------ Select Heuristic Type ------")
    print("  1 - Manhattan Distance")
    print("  2 - Misplaced Tiles")

def get_heuristic_choice():
    display_heuristic_options()
    choice = input("Select heuristic option: ")
    if choice == "1":
        return "manhattan_distance"
    elif choice == "2":
        return "misplaced_tiles"
    else:
        print("Invalid option. Using Manhattan Distance as default.")
        return "manhattan_distance"

def display_searchs_name(board_size):
    names = ["BFS", "DFS", "IDS", "Greedy", "A*"]
    if(board_size == 5):
        print(f"1 - {names[3]}")
        print(f"2 - {names[4]}")
        print(f"0 - Back")
    else:
        for i in range(len(names)):
            print(f"{i + 1} - {names[i]}")
        print("0 - Back")

def swithc_searchs(board_sizes, input, problem):
    if(board_sizes < 5):
        match input:
            case "1" : 
                breadthFirstSearch(problem)
                print("Open the directory data_test/breadthfirstsearch_resolucao.txt")
                pause_clean(2)
            case "2" : 
                depthFirstSearch(problem)
                print("Open the directory data_test/depthfirstsearch_resolucao.txt")
                pause_clean(2)
            case "3" : 
                iterativeDepthSearch(problem)
                print("Open the directory data_test/ids_resolucao.txt")
                pause_clean(2)
            case "4" : 
                heuristic = get_heuristic_choice()
                greedySearch(problem, heuristic)
                print("Open the directory data_test/greedysearch_resolucao.txt")
                pause_clean(2)
            case "5" : 
                heuristic = get_heuristic_choice()
                aStarSearch(problem,heuristic)
                print("Open the directory data_test/a*_resolucao.txt")
                pause_clean(2)
            case "0" :
                return False
            case _   : 
                print("Invalid option. Please try again.")
    else:
        match input:
            case "1" : 
                greedySearch(problem)
                print("Open the directory data_test/greedysearch_resolucao.txt")
                pause_clean(2)
            case "2" : 
                aStarSearch(problem)
                print("Open the directory data_test/a*_resolucao.txt")
                pause_clean(2)
            case _   : 
                print("Invalid option. Please try again.")

def execute_all_search(board_size, problem):
    print("For informed algorithms (Greedy and A*), select heuristic:")
    heuristic = get_heuristic_choice()
    pause_clean(1)

    searchs = [breadthFirstSearch, depthFirstSearch, iterativeDepthSearch, greedySearch, aStarSearch]
    if board_size < 5:
        for search in searchs:
            print(f"Runing {search.__name__}")
            if search.__name__ in ['greedySearch', 'aStarSearch']:
                search(problem, heuristic)
            else:
                search(problem)
            pause_clean(5, "Loading next search")
    else:
        # For 5x5, only informed searches
        for search in [greedySearch, aStarSearch]:
            print(f"Runing {search.__name__}")
            search(problem,heuristic)
            pause_clean(5, "Loading next search")
    pause_clean(1, "Executation complete!", False)

def pause_clean(pause_time, label=None, dots=True):
    if label != None and dots == True:
        dot_steps = ['.', '..', '...']
        total_steps = pause_time * len(dot_steps)
        for i in range(total_steps):
            dots = dot_steps[i % len(dot_steps)]
            print('\r' + label + dots + '   ', end='', flush=True)
            time.sleep(0.5)
        print('\r' + ' ' * (len(label) + 6), end='\r')  # Clear line
        os.system('cls' if os.name == 'nt' else 'clear')
    else :
        print(label)
        time.sleep(pause_time)
        os.system('cls' if os.name == 'nt' else 'clear')
