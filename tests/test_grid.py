
from grid.grid import Grid
import pytest

def test_grid_initialization():
    grid = Grid(5, 5, walls={(1, 1), (2, 2)})
    assert grid.width == 5
    assert grid.height == 5
    assert grid.walls == {(1, 1), (2, 2)}

def test_grid_no_walls():
    grid_no_walls = Grid(3, 3)
    assert grid_no_walls.width == 3
    assert grid_no_walls.height == 3
    assert grid_no_walls.walls == set()

def test_grid_dimensions_below_zero():
    with pytest.raises(ValueError, match="Width and height must be positive integers."):
        Grid(-2, -2, walls={(1, 1), (6, 6), (-1, -1)})

def test_grid_wall_out_of_bounds():
    with pytest.raises(ValueError, match="Wall position .* is out of bounds."):
        Grid(5, 5, walls={(1, 1), (6, 6), (-1, -1)})

def test_passable():
    grid = Grid(5, 5, walls={(1, 1), (2, 2)})
    assert grid.passable((0, 0)) == True
    assert grid.passable((1, 1)) == False
    assert grid.passable((2, 2)) == False
    assert grid.passable((3, 3)) == True
    assert grid.passable((-1, -1)) == False  # Out of bounds

def test_bounds():
    grid = Grid(5, 5)
    assert grid.in_bounds((0, 0)) == True
    assert grid.in_bounds((4, 4)) == True
    assert grid.in_bounds((5, 5)) == False
    assert grid.in_bounds((-1, 0)) == False

def test_neighbors():
    grid = Grid(5, 5, walls={(1, 1), (2, 2)})
    assert set(grid.neighbors((0, 0))) == {(1, 0), (0, 1)}
    assert set(grid.neighbors((1, 0))) == {(0, 0), (2, 0)} # (1, 1) is a wall
    assert set(grid.neighbors((1, 1))) == {(0, 1), (1, 0), (1, 2), (2, 1)}
    assert set(grid.neighbors((2, 2))) == {(1, 2), (2, 1), (3, 2), (2, 3)}
    assert set(grid.neighbors((2, 3))) == {(3, 3), (2, 4), (1, 3)}  # (2, 2) is a wall
    assert set(grid.neighbors((-1, -1))) == set()  # Out of bounds without neighboring positions in bounds
