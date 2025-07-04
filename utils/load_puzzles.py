import json

def load_puzzles(path_json):
    with open(path_json, "r") as file:
        data = json.load(file)
    return data