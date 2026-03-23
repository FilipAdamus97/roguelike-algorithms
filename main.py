from grid import Grid
from pathfinding import astar, bfs
from renderer import Renderer
from dungeon import generate_dungeon

def main():
    print("Script started successfully.")
    walls = {(0,3), (1, 1), (1, 2), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)}
    grid = Grid(10, 10, walls)

    start = (0, 0)
    goal = (9, 9)

    path = bfs(start, goal, grid)
    print(path)
    print("BFS path length:", len(path) if path else "No path found.\n")

    renderer = Renderer(grid)
    renderer.render(path)

    path = astar(start, goal, grid)
    print(path)
    print("BFS path length:", len(path) if path else "No path found.\n")

    renderer.render(path)

    dungeon = generate_dungeon(40, 40, 6)
    renderer = Renderer(grid=dungeon)
    renderer.render()

    print("Script finished successfully.")
if __name__ == "__main__":
    main()
