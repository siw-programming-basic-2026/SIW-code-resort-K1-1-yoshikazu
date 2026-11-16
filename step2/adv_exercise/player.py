def get_move(command):
    """入力を (x の変化量, y の変化量) に変換する。 / Convert input to (change in x, change in y)."""
    moves = {
        "w": (0, -1),
        "a": (-1, 0),
        "s": (0, 1),
        "d": (1, 0),
    }
    return moves.get(command)


class Player:
    def __init__(self, name="プレイヤー", x=1, y=1, money=1000, turn=0):
        self.name = name
        self.x = x
        self.y = y
        self.money = money
        self.turn = turn

    def show(self):
        print(f"名前: {self.name}")
        print(f"所持金: {self.money}")
        print(f"位置: x={self.x}, y={self.y}")
        print(f"ターン: {self.turn}")

    def can_move(self, casino_map, x, y):
        if not (0 <= y < len(casino_map)):
            return False
        if not (0 <= x < len(casino_map[y])):
            return False
        return casino_map[y][x] != "#"

    def move(self, casino_map, movement):
        """移動成功時だけ座標とターンを更新する。 / Update coordinates and turn only when movement succeeds."""
        dx, dy = movement
        next_x = self.x + dx
        next_y = self.y + dy
        if (dx == 0 and dy == 0) or not self.can_move(casino_map, next_x, next_y):
            return False

        # TODO 1: 移動成功時に self.x, self.y, self.turn を更新して True を返す。
        # TODO 1: On successful movement, update self.x, self.y and self.turn, then return True.
        return False
