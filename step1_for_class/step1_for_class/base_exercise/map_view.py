def show_map(casino_map, player):
    for y in range(len(casino_map)):
        line = ""
        for x in range(len(casino_map[y])):
            # TODO 2: x と y がプレイヤーの座標と両方一致したら、 / TODO 2: When both x and y match the player coordinates,
            # "@" を line に追加する。それ以外はマップの記号を追加する。 / append "@" to line; otherwise append the map symbol.
            # 今はマップの記号だけを表示している。 / Currently only map symbols are displayed.
            if player['x']==x and player['y']==y:
                line+="@"
            else:
                line += casino_map[y][x]
        print(line)