from player import get_move


def read_command():
    return input("移動 w/a/s/d、終了 q > ").strip().lower()


def handle_command(casino_map, player, command):
    """続ける場合は True、終了する場合は False を返す。 / Return True to continue, or False to quit."""
    if command == "q":
        print("終了します。")
        return False

    movement = get_move(command)
    if movement is None:
        print("w/a/s/d または q を入力してください。")
    elif player.move(casino_map, movement):
        print("移動しました。")
    else:
        print("壁またはマップ外には移動できません。")
    return True
