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
    moves = {
        "w": (0, -1),
        # TODO 1: a は左、s は下、d は右。変化量を完成させる。 / TODO 1: a moves left, s down and d right. Complete the coordinate changes.
        "a": (0, 0),
        "s": (0, 0),
        "d": (0, 0),
    }
    return moves.get(command)


def can_move(casino_map, x, y):
    # 負の添字は末尾を参照するため、必ず先に範囲を確認する。 / Check bounds first because negative indices access elements from the end.
    if not (0 <= y < len(casino_map)):
        return False
    if not (0 <= x < len(casino_map[y])):
        return False
    # TODO 2: 壁以外なら True、壁なら False を返す。 / TODO 2: Return True for non-wall cells and False for walls.
    # 範囲の確認は上で完成済み。今はすべての移動を拒否する。 / Bounds checks are complete above. Currently all movement is rejected.
    return False


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
