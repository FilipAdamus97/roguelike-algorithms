class Grid:
    """A simple grid class to represent the environment for pathfinding algorithms."""
    def __init__(self, width: int, height: int, walls: set[tuple[int, int]] | None = None):
        """Initialize the grid with given dimensions and walls."""

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        self.width = width
        self.height = height

        if walls:
            for wall in walls:
                if not self.in_bounds(wall):
                    raise ValueError(f"Wall position {wall} is out of bounds.")
        self.walls = set(walls) if walls else set()

    def in_bounds(self, pos: tuple[int, int]) -> bool:
        """Check if a position is within the bounds of the grid."""
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos: tuple[int, int]) -> bool:
        """Check if a position is not a wall."""
        return pos not in self.walls and self.in_bounds(pos)

    def neighbors(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        """Return a list of neighboring positions (excluding diagonals) that are in bounds and passable."""
        x, y = pos
        directions = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

        results = filter(self.in_bounds, directions)
        results = filter(self.passable, results)
        return list(results)

    def reverse_fields(self):
        """Return a new grid with walls and open spaces reversed."""
        new_walls = set()
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) not in self.walls:
                    new_walls.add((x, y))
        return Grid(self.width, self.height, new_walls)
