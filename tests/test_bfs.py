from grid import Grid
from pathfinding import bfs

def test_bfs_simple_path():
    grid = Grid(5, 5)
    start = (0, 0)
    goal = (4, 4)
    path = bfs(start, goal, grid)
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) == 9  # Minimum steps from (0, 0) to (4, 4) in a grid without walls

def test_bfs_with_walls():
    grid = Grid(5, 5, walls={(1, 0), (1, 1), (1, 2), (1, 3), (3, 4), (3, 3), (3, 2), (3, 1)})
    start = (0, 0)
    goal = (4, 4)
    path = bfs(start, goal, grid)
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) > 9  # Path should be longer due to walls

def test_bfs_no_path():
    grid = Grid(5, 5, walls={(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)})
    start = (0, 0)
    goal = (4, 4)
    path = bfs(start, goal, grid)
    assert path is None  # No path should exist due to walls blocking the way

def test_bfs_start_equals_goal():
    grid = Grid(5, 5)
    start = (2, 2)
    goal = (2, 2)
    path = bfs(start, goal, grid)
    assert path is not None
    assert path == [start]  # Path should contain only the start/goal position

def test_bfs_goal_out_of_bounds():
    grid = Grid(5, 5)
    start = (0, 0)
    goal = (5, 5)  # Out of bounds
    path = bfs(start, goal, grid)
    assert path is None  # No path should exist due to out of bounds goal

def test_bfs_start_out_of_bounds():
    grid = Grid(5, 5)
    start = (-1, -1)  # Out of bounds
    goal = (4, 4)
    path = bfs(start, goal, grid)
    assert path is None  # No path should exist due to out of bounds start