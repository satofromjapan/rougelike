class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

def creat_room(game_map, room):
    # go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            game_map.walkable[x, y] = True
            game_map.transparent[x, y] = True

def make_map(game_map):
    # Create two rooms for demonstration purposes
    
