from map_data import create_map
from map_view import show_map
from player import create_player, show_player


def main():
    casino_map = create_map()
    player = create_player()

    print("=== Python Casino / STEP 1 ===")
    show_map(casino_map, player)
    print()
    show_player(player)


if __name__ == "__main__":
    main()
