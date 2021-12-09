class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<position: [{}, {}]>".format(self.x, self.y)

    def clone(self):
        return Position(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_adjacent_list(self):
        adjacent_pos_list = [
            Position(self.x, self.y - 1),
            Position(self.x + 1, self.y),
            Position(self.x, self.y + 1),
            Position(self.x - 1, self.y)
        ]
        return adjacent_pos_list

    def is_adjacent(self, other) -> bool:
        adjacent_pos_list = self.get_adjacent_list()
        return other in adjacent_pos_list
