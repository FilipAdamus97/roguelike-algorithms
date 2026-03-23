from grid import Grid

class Renderer:
    """A simple renderer to visualize the grid and the pathfinding process."""
    def __init__(self, grid: Grid | None = None, legend: dict[str, str] | None = None):
        default_legend = {
            "Wall": "#",
            "Start": "S",
            "End": "E",
            "Path": "*",
            "Empty": "."
        }
        self.legend = {**default_legend, **legend} if legend else default_legend
        self.grid = grid if grid is not None else Grid(10, 10) # Default grid size

    def render(self, path: list[tuple[int, int]] | None = None, start: tuple[int, int] | None = None, end: tuple[int, int] | None = None):
        """Render the grid and provided path to the console."""
        if path is None:
            path_set = set() # No path, so empty set
        else:
            path_set = set(path) # For faster lookup

        if start is None:
            start = path[0] if path else None # Default to first path position if available

        if end is None:
            end = path[-1] if path else None # Default to last path position if available

        for y in range(self.grid.height):
            row = []
            for x in range(self.grid.width):
                pos = (x, y)
                if not self.grid.passable(pos):
                    row.append(self.legend["Wall"])
                elif start is not None and pos == start:
                    row.append(self.legend["Start"])
                elif end is not None and pos == end:
                    row.append(self.legend["End"])
                elif pos in path_set:
                    row.append(self.legend["Path"])
                else:
                    row.append(self.legend["Empty"])
            print("".join(row))
        print() # Add an empty line after last row for better readability