import heapq
from grid import Grid
from pathfinding import reconstruct_path

def astar(
        start: tuple[int, int],
        goal: tuple[int, int],
        grid: Grid
        ) -> list[tuple[int, int]] | None:
    """Perform A* search to find the shortest path from start to goal on the grid."""
    if not grid.in_bounds(start) or not grid.in_bounds(goal):
        raise ValueError("Start and goal positions must be within the bounds of the grid.")

    if start == goal:
        return [start]

    # A*:
    # priority -> f(n) = priority of node n
    # cost_so_far -> g(n) + cost from start to n
    # heuristic -> h(n) heuristic function (Manhattan distance)

    frontier = []
    cost_so_far = {start: 0}
    came_from = {start: None}
    start_priority = heuristic(start, goal)
    heapq.heappush(frontier, (start_priority, start))

    while frontier:
        current_priority, current = heapq.heappop(frontier)

        if current == goal:
            break

        if current_priority > cost_so_far[current] + heuristic(current, goal):
            continue

        for neighbor in grid.neighbors(current):
            new_cost = cost_so_far[current] + 1  # Assuming uniform cost for moving to a neighbor
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)

def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Calculate the Manhattan distance heuristic between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
