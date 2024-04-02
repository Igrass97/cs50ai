from frontier import StackFrontier, QueueFrontier, AStarFrontier
from node import Node

def get_all_transition_models(maze, current, frontier, explored):
    row = current.state[0]
    column = current.state[1]
    
    transition_models = []

    movements = [
        ("↓", [row + 1, column]),
        ("↑", [row - 1, column]),
        ("→", [row, column + 1]),
        ("←", [row, column - 1])
    ]
    
    in_boundary = filter(lambda x: not maze.is_out_of_boundary(x[1]), movements)
    
    for movement in in_boundary:
        position = movement[1]
        
        if not maze.is_wall(position) and not maze.is_out_of_boundary(position) and not frontier.contains_state(position) and position not in explored:
            transition_models.append(movement)
            
    
    return transition_models

def solve(maze):    
    token_positions = maze.find_start_end()

    frontier = AStarFrontier()
    initial_node = Node(state=token_positions['start_pos'], parent=None, action=None, heuristic_value=manhattan_distance(token_positions['start_pos'], token_positions['end_pos']), path_cost=0)
    frontier.add(initial_node)
    solution = None
    explored = []

    while not frontier.empty() and not solution:
        current = frontier.remove()
        explored.append(current.state)
        row = current.state[0]
        column = current.state[1]
        
        if maze.rows[row][column] == 'B':
            solution = current
        else:            
            transition_models = get_all_transition_models(maze, current, frontier, explored)

            for transition_model in transition_models:
                state = transition_model[1]
                frontier.add(Node(state=state, parent=current, action=transition_model[0], heuristic_value=manhattan_distance(state, token_positions['end_pos']), path_cost=current.path_cost + 1))

                
    if solution:
        print('Solution')
        steps = [[solution.action, solution.state]]
        current = solution
        
        while current.parent.action:
            steps.append([current.parent.action, current.parent.state])
            current = current.parent

        return explored
        
def manhattan_distance(start, end):
    distance_x = abs(end[0] - start[0])
    distance_y = abs(end[1] - start[1])
    
    return distance_x + distance_y