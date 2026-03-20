from grid import Grid

class Renderer:
    """A simple renderer to visualize the grid and the pathfinding process."""
    def __init__(self, grid: Grid | None = None, legend: dict[str, str] | None = None):
        self.legend = legend if legend is not None else { # Default legend
            "Wall": "#",
            "Start": "S",
            "End": "E",
            "Path": "*",
            "Empty": "."
        }    

        self.grid = grid if grid is not None else Grid(10, 10) # Default grid size

    def render(self, path: list[tuple[int, int]] | None = None):
        """Render the grid and provided path to the console."""
        path_set = set(path) if path else set() # For faster lookup

        for y in range(self.grid.height):
            row = []
            for x in range(self.grid.width):
                pos = (x, y)
                if self.grid.in_bounds(pos):
                    if not self.grid.passable(pos):
                        row.append(self.legend["Wall"])
                    elif path and path[0] == pos:
                        row.append(self.legend["Start"])
                    elif path and path[-1] == pos:
                        row.append(self.legend["End"])  
                    elif path and pos in path_set:
                        row.append(self.legend["Path"])
                    else:
                        row.append(self.legend["Empty"])
                else:
                    row.append("?") # Unknown case
            print("".join(row))