import random

NORMAL_SHIPS = {1: 3, 2: 2, 3: 1}

class ShipError(BaseException):
    pass


class Ship():
    def __init__(self, coords):
        self.length = len(coords)
        self.coords = coords
        self.health = len(coords)

    def dict(self):
        return {'self.length': self.length,
        'self.coords': self.coords,
        'self.health': self.health}

    @staticmethod
    def set_coords(playfield):
        coords = list()
        while True:
            try:
                length = int(input("Введите длину от 1 до 3:"))
            except ValueError:
                print("Некорректная длина. Введите число!")
                continue
            if playfield.ships_count[length] == NORMAL_SHIPS[length]:
                print("Кораблей такой длины уже достаточно.")
                continue
            if length in [1, 2, 3]:
                print("Вводите координаты без пробелов (например, 23).")
                break
            print("Некорректная длина")
        print(playfield)
        for i in range(length):
            while True:
                coord_str = list(input(f"Введите {i + 1}-ю координату."
                                       f"Если хотите начать заново введите 0\n"))
                if coord_str == 0:
                    continue
                if len(coord_str) != 2:
                    print("Вводите координаты без пробелов (например, 23)!")
                    continue
                try:
                    coord = [int(digit) for digit in coord_str]
                    if not all([0 < i < 7 for i in coord]):
                        raise ShipError("Координаты не соответствуют игровому полю")
                except ValueError:
                    print("Введите 2 цифры!")
                    continue
                except ShipError as ex:
                    print(ex)
                    continue
                if coord in coords:
                    print("Вы уже ввели эти координаты")
                if playfield.box[coord[0]-1][coord[1]-1] == "О":
                    coords.append(coord)
                    break
                else:
                    print("Поле занято")
        if Ship.check_coords(playfield, coords) and coords is not None:
            playfield.ships.append(Ship(coords))
            playfield.ships_count[length] += 1
            for i in coords:
                playfield.box[i[0]-1][i[1]-1] = '■'
            print(playfield)
        else:
            print("Заново")
            Ship.set_coords(playfield)

    @staticmethod
    def auto_coords(playfield):
        coords = list()
        while True:
            length = random.randint(1, 3)
            if playfield.ships_count[length] == NORMAL_SHIPS[length]:
                continue
            break
        for i in range(length):
            while True:
                coord = [random.randint(1, 6), random.randint(1, 6)]
                if playfield.box[coord[0] - 1][coord[1] - 1] == "О" and coord not in coords:
                    coords.append(coord)
                    break
        if Ship.check_coords(playfield, coords, auto=True) and coords is not None:
            playfield.ships.append(Ship(coords))
            playfield.ships_count[length] += 1
            for i in coords:
                playfield.box[i[0] - 1][i[1] - 1] = '■'
        else:
            Ship.auto_coords(playfield)

    @staticmethod
    def check_coords(playfield, coords, auto=False):
        check_list, horizontal, vertical = [], set(), set()
        for crd in coords:
            check_list.append(playfield.box[crd[0]-1][crd[1]-1] == "О")
            if crd[0] != 1:
                check_list.append(playfield.box[crd[0]-2][crd[1]-1] == "О")
            if crd[0] != 6:
                check_list.append(playfield.box[crd[0]][crd[1]-1] == "О")
            if crd[1] != 1:
                check_list.append(playfield.box[crd[0]-1][crd[1]-2] == "О")
            if crd[1] != 6:
                check_list.append(playfield.box[crd[0]-1][crd[1]] == "О")
            horizontal.add(crd[0])
            vertical.add(crd[1])
        check_list.append(len(horizontal) == 1 or len(vertical) == 1)
        if len(horizontal) == 1:
            srt = sorted(vertical)
            count = srt[0] - 1
            for i in srt:
                check_list.append(i - count == 1)
                count += 1
        elif len(vertical) == 1:
            srt = sorted(horizontal)
            count = srt[0] - 1
            for i in srt:
                check_list.append(i - count == 1)
                count += 1
        if not all(check_list):
            if not auto:
                print("Вы ввели некорректные координаты. Корабль должен быть прямым,\n"
                      "а также не стоять вплотную к другим кораблям. Допускается соседство с\n"
                      "кораблём по диагонали.")
            return False
        if not auto:
            print("Корабль добавлен")
        return True

if __name__ == "__main__":
    pass