from commands import read_command, handle_command
from map_data import create_map
from map_view import show_map
from player import create_player, show_player


def main():
    casino_map = create_map()
    player = create_player()
    print("=== Python Casino / STEP 2 ===")

    while True:
        show_map(casino_map, player)
        show_player(player)
        command = read_command()
        if not handle_command(casino_map, player, command):
            break


if __name__ == "__main__":
    main()
