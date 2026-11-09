from map_data import create_map
from map_view import show_map
from player import create_player, show_player


def main():
    casino_map = create_map()
    # 発展課題（任意）: create_player に引数を追加した場合は、ここで初期値を渡す。
    # Optional extension: If you add parameters to create_player, pass the initial values here.
    player = create_player()

    print("=== Python Casino / STEP 1 ===")
    show_map(casino_map, player)
    print()
    show_player(player)
yoshikaz

if __name__ == "__main__":
    main()
