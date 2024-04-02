# Stack frontier will produce a depth first search algorithm
class StackFrontier():
    def __init__(self):
        self.frontier = []
        # self.heuristic = heuristic

    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    # def order_by_heuristic(self):
    #     self.frontier = sorted(self.frontier, self.heuristic)
        
# Queue frontier will produce a breadth first search algorithm
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# AStarFrontier will produce an A* search algorithm, sorting the nodes by the heuristic value + path cost before removing
class AStarFrontier(QueueFrontier):
    def __init__(self):
        super().__init__()
        
    def remove(self):
        self.frontier = sorted(self.frontier, key=lambda node: (node.path_cost + node.heuristic_value))
        return super().remove()