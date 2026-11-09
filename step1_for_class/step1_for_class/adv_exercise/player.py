class Player:
    def __init__(self, name="プレイヤー",x=1,y=1,money=1000):
        self.name=name
        self.x=x
        self.y=y
        self.money=money


    def show_info(self):
        print(f"名前: {self.name}")
        print(f"所持金: {self.money}")
        print(f"位置: x={self.x}, y={self.y}")
