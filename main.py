from grid import Grid
from pathfinding import bfs
from renderer import Renderer

def main():
    print("Script started successfully.")
    walls = {(1, 1), (1, 2), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)}
    grid = Grid(10, 10, walls)

    start = (0, 0)
    goal = (9, 9)

    path = bfs(start, goal, grid)
    print(path)

    renderer = Renderer(grid)
    renderer.render(path)
    print("Script finished successfully.")

if __name__ == "__main__":
    main()
