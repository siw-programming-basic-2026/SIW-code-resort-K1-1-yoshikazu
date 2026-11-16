def create_player():
    return {
        "name": "プレイヤー",
        "x": 1,
        "y": 1,
        "money": 1000,
        "turn": 0,
    }


def show_player(player):
    print(f"名前: {player['name']}")
    print(f"所持金: {player['money']}")
    print(f"位置: x={player['x']}, y={player['y']}")
    print(f"ターン: {player['turn']}")


def get_move(command):
    """入力を (x の変化量, y の変化量) に変換する。 / Convert input to (change in x, change in y)."""
    # TODO: a/s/d の変化量を完成させる
    # TODO: complete coordinate changes for a/s/d
    moves = {
        'w': (0, -1),
        'a': (-1, 0),
        's': (0, 1),
        'd': (1, 0),
    }
    return moves.get(command)


def can_move(casino_map, x, y):
    if not (0 <= y < len(casino_map)):
        return False
    if not (0 <= x < len(casino_map[y])):
        return False
    # TODO: 壁ならFalse、それ以外はTrue
    # TODO: return False for walls, True otherwise
    #if casino_map[y][x] !="#":
     #   return True
    #return False
    #または
    return casino_map[y][x]!="#"


def move_player(casino_map, player, movement):
    dx, dy = movement
    next_x = player["x"] + dx
    next_y = player["y"] + dy
    if (dx == 0 and dy == 0) or not can_move(casino_map, next_x, next_y):
        return False
    player["x"] = next_x
    player["y"] = next_y
    player["turn"] += 1
    return True
