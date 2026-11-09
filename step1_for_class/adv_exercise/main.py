from map_data import create_map
from map_view import show_map
from player import Player


def main():
    casino_map = create_map()
    player = Player(name="yoshikazu",x=1,y=1,money=1000)
    player2 = Player(name="Ito",x=8,y=6,money=500)

    print("=== Python Casino / STEP 1 ===")
    show_map(casino_map, player)
    print()
    player.show_info()

    show_map(casino_map,player2)
    player2.show_info()


if __name__ == "__main__":
    main()
