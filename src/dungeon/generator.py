import random
from grid import Grid
from pathfinding import bfs

def generate_dungeon(width: int, height: int, number_of_rooms: int = 4) -> Grid:
    """Generate a simple dungeon layout using a grid."""
    dungeon = Grid(width, height)
    dungeon = dungeon.reverse_fields()  # Start with all walls
    rooms = []
    while len(rooms) < number_of_rooms:
        overlaps = False
        room_width = random.randint(3, 8)
        room_height = random.randint(3, 8)
        x = random.randint(0, width - room_width - 1)
        y = random.randint(0, height - room_height - 1)

        for existing_room in rooms:
            if (x < existing_room[0] + existing_room[2] + 1 and
                x + room_width > existing_room[0] - 1 and
                y < existing_room[1] + existing_room[3] + 1 and
                y + room_height > existing_room[1] - 1):
                overlaps = True
                break

        if not overlaps:
            rooms.append((x, y, room_width, room_height))

    for room in rooms:
        carve_room(room, dungeon)
    connect_rooms(rooms, dungeon)
    return dungeon

def carve_room(room: tuple[int, int, int, int], dungeon: Grid):
    """Carve out a room in the dungeon grid."""
    x, y, room_width, room_height = room
    for i in range(x, x + room_width):
        for j in range(y, y + room_height):
            dungeon.walls.discard((i, j))  # Remove walls to create open space

def carve_corridor(start: tuple[int, int], end: tuple[int, int], dungeon: Grid):
    """Carve a corridor between two points in the dungeon grid."""
    if random.choice([True, False]):
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            dungeon.walls.discard((x, start[1]))  # Carve horizontal corridor
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            dungeon.walls.discard((end[0], y))  # Carve vertical corridor
    else:
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            dungeon.walls.discard((start[0], y))  # Carve vertical corridor
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            dungeon.walls.discard((x, end[1]))  # Carve horizontal corridor

def room_center(room: tuple[int, int, int, int]) -> tuple[int, int]:
    """Return the center points of the rooms."""
    x, y, room_width, room_height = room
    return (x + room_width // 2, y + room_height // 2)

def connect_rooms(rooms: list[tuple[int, int, int, int]], dungeon: Grid):
    """Connect all rooms in the dungeon with corridors."""
    for i in range(len(rooms) - 1):
        room_a = rooms[i]
        room_b = rooms[i + 1]
        start = room_center(room_a)
        end = room_center(room_b)
        carve_corridor(start, end, dungeon)
