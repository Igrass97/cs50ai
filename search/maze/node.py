class Node():
    def __init__(self, state, parent, action, heuristic_value, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic_value = heuristic_value
        self.path_cost = path_cost
