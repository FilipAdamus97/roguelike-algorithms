from collections import deque
from grid import Grid

def bfs(
        start: tuple[int, int],
        goal: tuple[int, int],
        grid: Grid
        ) -> list[tuple[int, int]] | None:
    """Perform Breadth-First Search (BFS) to find the shortest path from start to goal on the grid."""
    if not grid.in_bounds(start) or not grid.in_bounds(goal):
        raise ValueError("Start and goal positions must be within the bounds of the grid.")

    if start == goal:
        return [start]

    frontier = deque([start])
    came_from = {start: None}

    while frontier:
        current = frontier.popleft()

        if current == goal:
            break

        for neighbor in grid.neighbors(current):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

def reconstruct_path(
        came_from: dict[tuple[int, int], tuple[int, int] | None],
        start: tuple[int, int],
        goal: tuple[int, int]
        ) -> list[tuple[int, int]] | None:
    """Reconstruct the path from start to goal using the came_from dictionary."""
    if goal not in came_from:
        return None

    current = goal
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path
