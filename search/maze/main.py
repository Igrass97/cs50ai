from maze import Maze
from solve import solve
from animate import generate_animation

maze = Maze('maze2.txt')

movements = solve(maze)

generate_animation(maze.rows, movements)