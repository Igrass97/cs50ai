from maze import Maze
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib

def generate_animation(maze_rows, movements):
    maze_matrix = np.array(maze_rows)

    # Create a figure and axis
    fig, ax = plt.subplots()
    # fig.siz(8, 6)

    # Set a colormap
    cmap = matplotlib.cm.get_cmap('cividis', 5)

    # Create a numerical array for the maze
    maze_numeric = np.zeros_like(maze_matrix, dtype=int)
    maze_numeric[maze_matrix == ' '] = 0  # Free spaces
    maze_numeric[maze_matrix == '#'] = 2  # Walls
    maze_numeric[maze_matrix == 'A'] = 1  # Start
    maze_numeric[maze_matrix == 'B'] = 3  # End
    maze_numeric[maze_matrix == 'X'] = 4  # Visited

    # Initialize the plot
    img = ax.imshow(maze_numeric, cmap=cmap, vmin=0, vmax=4, interpolation='none')
    ax.axis('off')

    start_pos = np.argwhere(maze_matrix == 'A')[0]
    end_pos = np.argwhere(maze_matrix == 'B')[0]
    ax.text(start_pos[1], start_pos[0], 'A', ha='center', va='center', color='blue', fontsize=12)
    ax.text(end_pos[1], end_pos[0], 'B', ha='center', va='center', color='green', fontsize=12)

    # Function to update the plot for each frame
    def update(frame):
        global current_pos
        if frame < len(movements):
            move = np.array(movements[frame], dtype=int)  # Convert move to NumPy array with integer dtype
            maze_numeric[move[0], move[1]] = 4  # Mark the current position as visited
            print(maze_numeric)
            current_pos = move  # Update current position
            img.set_data(maze_numeric)
            return [img]

    # Initialize current position at 'A'
    current_pos = start_pos

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=len(movements), blit=True, interval=100)

    # Save the animation as a GIF using Imagemagick
    anim.save('maze_animation.gif', writer='imagemagick', fps=10)