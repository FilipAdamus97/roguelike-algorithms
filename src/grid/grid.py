class Grid:
    """A simple grid class to represent the environment for pathfinding algorithms."""
    def __init__(self, width: int, height: int, walls: set[tuple[int, int]] | None = None):
        """Initialize the grid with given dimensions and walls."""
        self.width = width
        self.height = height
        self.walls = set(walls) if walls else set()

    def in_bounds(self, pos: tuple[int, int]) -> bool:
        """Check if a position is within the bounds of the grid."""
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos: tuple[int, int]) -> bool:
        """Check if a position is not a wall."""
        return pos not in self.walls

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
    