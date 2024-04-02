
from utils.parse_txt_maze import parse_txt_maze

START_CHAR = 'A'
END_CHAR = 'B'

class Maze():
    rows = []
    width = 0
    height = 0

    def __init__(self, filename):
        parsed_maze_data = parse_txt_maze(filename)

        self.height = parsed_maze_data['height']
        self.width = parsed_maze_data['width']
        self.rows = parsed_maze_data['rows']
        
    def find_start_end(self):
        start_pos = [0, 0]
        end_pos = [0, 0]

        for i, row in enumerate(self.rows):
            for j, char in enumerate(row):
                if char == START_CHAR:
                    start_pos = [i, j]
                if char == END_CHAR:
                    end_pos = [i, j]

        return {
            'start_pos': start_pos,
            'end_pos': end_pos
        }
        
    
    def is_wall(self, position):
        return self.rows[position[0]][position[1]] == '#'
    
    def is_out_of_boundary(self, position):
        if position[0] < 0 or position[1] < 0:
            return True
        
        if position[0] >= self.height or position[1] >= self.width:
            return True
        
        return False