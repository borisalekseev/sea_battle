from Ship import Ship
import random

class PlayFieldError(BaseException):
    pass

class PlayField:
    def __init__(self, name, auto=False):
        self.name = name
        self.box = [['О' for i in range(6)] for j in range(6)]
        self.hidden = [['О' for i in range(6)] for j in range(6)]
        self.ships_count = {1: 0, 2: 0, 3: 0}
        self.ships = []
        self.beaten = False
        self.all_auto_coords = [[i, j] for i in range(1, 7) for j in range(1, 7)]
        random.shuffle(self.all_auto_coords)
        if not auto:
            for i in range(6):
                self.add_ship()
        else:
            for i in range(6):
                self.auto_ship()

    def add_ship(self):
        Ship.set_coords(self)

    def check(self):
        while True:
            print(self.hidden_show())
            coord_str = list(input(f"Введите координаты: "))
            if len(coord_str) != 2:
                print("Вводите координаты без пробелов (например, 23)!")
                continue
            try:
                coord = [int(digit) for digit in coord_str]
                if not all([0 < i < 7 for i in coord]):
                    raise PlayFieldError("Координаты не соответствуют игровому полю")
            except ValueError:
                print("Введите 2 цифры!")
                continue
            except PlayFieldError as ex:
                print(ex)
                continue
            break
        if self.box[coord[0] - 1][coord[1] - 1] == "О":
            print("Мимо!")
            self.box[coord[0] - 1][coord[1] - 1] = "Y"
            self.hidden[coord[0] - 1][coord[1] - 1] = "Y"
        elif self.box[coord[0] - 1][coord[1] - 1] == '■':
            for ship in self.ships:
                if coord in ship.coords:
                    if ship.health > 1:
                        print("Ранен!")
                        self.box[coord[0] - 1][coord[1] - 1] = 'Х'
                        self.hidden[coord[0] - 1][coord[1] - 1] = "X"
                        ship.health -= 1
                        self.beaten = True if not sum([i.health for i in self.ships]) else False
                        return True
                    elif ship.health == 1:
                        print("Убит!")
                        self.box[coord[0] - 1][coord[1] - 1] = 'Х'
                        self.hidden[coord[0] - 1][coord[1] - 1] = "X"
                        ship.health -= 1
                        self.beaten = True if not sum([i.health for i in self.ships]) else False
                        return True
        elif self.box[coord[0] - 1][coord[1] - 1] == 'Х' or self.box[coord[0] - 1][coord[1] - 1] == "Y":
            print("Вы уже били это поле!")
            self.check()



    def auto_check(self):
        print(self)
        coord = self.all_auto_coords.pop()
        print(f"Компьютер бьёт по {self.name}: {''.join([*map(str, coord)])}")
        if self.box[coord[0] - 1][coord[1] - 1] == "О":
            print("Мимо!")
            self.box[coord[0] - 1][coord[1] - 1] = "Y"
            self.hidden[coord[0] - 1][coord[1] - 1] = "Y"
        elif self.box[coord[0] - 1][coord[1] - 1] == '■':
            for ship in self.ships:
                if coord in ship.coords:
                    if ship.health > 1:
                        print("Ранен!")
                        self.box[coord[0] - 1][coord[1] - 1] = 'Х'
                        self.hidden[coord[0] - 1][coord[1] - 1] = "X"
                        ship.health -= 1
                        self.beaten = True if not sum([i.health for i in self.ships]) else False
                        return True
                    elif ship.health == 1:
                        print("Убит!")
                        self.box[coord[0] - 1][coord[1] - 1] = 'Х'
                        self.hidden[coord[0] - 1][coord[1] - 1] = "X"
                        ship.health -= 1
                        self.beaten = True if not sum([i.health for i in self.ships]) else False
                        return True

    def auto_ship(self):
        Ship.auto_coords(self)

    def hidden_show(self):
        count, show = 1, '  1|2|3|4|5|6\n'
        for string in self.hidden:
            show += f"{count} {'|'.join(string)}\n"
            count += 1
        return show

    @staticmethod
    def auto_field():
        pass

    def __str__(self):
        count, show = 1, '  1|2|3|4|5|6\n'
        for string in self.box:
            show += f"{count} {'|'.join(string)}\n"
            count += 1
        return show


if __name__ == "__main__":
    pass
