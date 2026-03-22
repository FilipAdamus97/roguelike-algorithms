from grid import Grid
from renderer import Renderer
from pathfinding import bfs

def test_renderer_initialization():
    grid = Grid(5, 5, walls={(1, 1), (2, 2)})
    legend = {
        "Wall": "#",
        "Start": "S",
        "End": "E",
        "Path": "*",
        "Empty": "."
    }
    renderer = Renderer(grid=grid, legend=legend)
    assert renderer.grid == grid
    assert renderer.legend == legend

def test_renderer_render_custom_legend(capsys):
    grid = Grid(3, 3, walls={(1, 1)})
    legend = {
        "Wall": "X",
        "Start": "A",
        "End": "B",
        "Path": "+",
        "Empty": "-"
    }
    renderer = Renderer(grid=grid, legend=legend)
    path = bfs((0, 0), (2, 2), grid)
    assert path is not None  # Ensure a path is found
    renderer.render(path=path)
    captured = capsys.readouterr()
    expected_output = (
        "A++\n"
        "-X+\n"
        "--B\n"
    )
    assert captured.out == expected_output

def test_renderer_render(capsys):
    grid = Grid(4, 4, walls={(1, 1), (2, 2)})
    renderer = Renderer(grid=grid)
    path = bfs((0, 0), (3, 3), grid)
    renderer.render(path=path)
    captured = capsys.readouterr()
    output = captured.out.splitlines()
    assert output[0][0] == "S"
    assert output[-1][-1] == "E"
    assert "*" in captured.out
    assert "#" in captured.out

def test_renderer_render_no_path(capsys):
    grid = Grid(4, 4, walls={(1, 1), (2, 2)})
    renderer = Renderer(grid=grid)
    renderer.render(path=None)
    captured = capsys.readouterr()
    assert "S" not in captured.out
    assert "E" not in captured.out
    assert "*" not in captured.out
    assert "#" in captured.out
    assert "." in captured.out

def test_renderer_render_none_path(capsys):
    grid = Grid(3, 3)
    renderer = Renderer(grid=grid)
    renderer.render(path=None)
    captured = capsys.readouterr()
    output = captured.out
    assert "S" not in output
    assert "E" not in output
    assert "*" not in output

def test_renderer_render_start_end_without_path(capsys):
    grid = Grid(3, 3)
    renderer = Renderer(grid=grid)
    start = (0, 0)
    end = (2, 2)
    renderer.render(path=None, start=start, end=end)
    captured = capsys.readouterr()
    output = captured.out
    assert "S" in output
    assert "E" in output
    assert "*" not in output