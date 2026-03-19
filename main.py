from grid import Grid
from pathfinding import bfs

def main():
    walls = {(1, 1), (2, 1), (3, 1)}
    grid = Grid(10, 10, walls)

    start = (0, 0)
    goal = (7, 5)

    path = bfs(start, goal, grid)
    print(path)


if __name__ == "__main__":
    main()
