# AI Fundamentals

This repo contains practical examples following [CS50AI](https://cs50.harvard.edu/ai/2020/) by Brian Yu.

For written theory visit [My Obsidian Notes](https://github.com/Igrass97/demoncodex/tree/main/IT/Software/Computer%20Science/AI)

## Search Algorithms

Search algorithms covered: Depth-First, Breadth-First, A*.

### Maze

Make sure to install requirements before running the maze.

`pip install -r requirements.txt`

#### Run animations and try different algorithms

The maze input should be a txt file in which:

1. Start position is described by the character 'A'.
2. End position is described by the character 'B'.
3. Walls are described by the character '#'.

I've included the three mazes that Brian Yu provided in the course resources.

To select a different maze, change the file path in line 5 of [main.py](./search/maze/main.py).

The type of search algorithm used is only defined by the type of frontier you use:

1. StackFrontier (Depth-First)
2. QueueFrontier (Breadth-First)
3. AStarFrontier (A*)

You can change the frontier class used in line 31 [solve.py](./search/maze/solve.py)

To generate the animated gif, run `python main.py`.

You might need to install extra stuff in your system to generate the gif.
