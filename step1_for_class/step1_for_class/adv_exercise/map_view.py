def show_map(casino_map, player):
    """元のマップを書き換えず、プレイヤーの位置だけ @ を表示する。 / Display @ at the player position without changing the original map."""
    for y in range(len(casino_map)):
        line = ""
        for x in range(len(casino_map[y])):
            if x == player.x and y == player.y:
                line += "@"
            else:
                line += casino_map[y][x]
        print(line)
