def create_player():
    """プレイヤーの状態を辞書にまとめる。 / Store the player state in a dictionary."""
    return {
        "name": "プレイヤー",
        "x": 1,
        "y": 1,
        "money": 1000,
    }


def show_player(player):
    print(f"名前: {player['name']}")
    print(f"所持金: {player['money']}")
    print(f"位置: x={player['x']}, y={player['y']}")
