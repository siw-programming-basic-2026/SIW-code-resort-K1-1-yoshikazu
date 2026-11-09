def extract_view(casino_map, player):
    """中心から上下左右2マスを抽出し、マップ外は壁で埋める。 / Extract two cells in each direction from the center; fill out-of-map cells with walls."""
    # TODO 3: プレイヤーの左上2マスの座標を計算する。 / TODO 3: Calculate the coordinates two cells above and left of the player.
    # 現在の仮の値では、表示範囲が固定されている。 / The current placeholder values keep the view fixed.
    start_x = 0
    start_y = 0

    view = []
    for y in range(start_y, start_y + 5):
        row = []
        for x in range(start_x, start_x + 5):
            if 0 <= y < len(casino_map) and 0 <= x < len(casino_map[y]):
                row.append(casino_map[y][x])
            else:
                row.append("#")
        view.append(row)
    return view


def show_map(casino_map, player):
    # extract_view は新しい二次元リストを返すので、元のマップは変わらない。 / extract_view returns a new two-dimensional list, leaving the original map unchanged.
    view = extract_view(casino_map, player)
    view[2][2] = "@"
    for row in view:
        print("".join(row))
