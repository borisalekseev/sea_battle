from PlayField import PlayField


class BrokenField(ValueError):
    pass


def main():
    pf = PlayField('player', auto=True)
    while True:
        try:
            cf = PlayField('computer', auto=True)
            break
        except RecursionError:
            # Я принял такое решение с пониманием, что так делать не всегда хорошо.
            # Очень уж хотелось использовать Ship.check_coords() и для игрока, и для компа.
            continue

    while True:
        while True:
            a = cf.auto_check() # игрок проверяет, возвращает True если попал
            if (not a) or cf.beaten:
                break
        if cf.beaten:
            print("pf win!")
            break
        while True:
            a = pf.auto_check() # комп проверяет
            if (not a) or pf.beaten:
                break
        if pf.beaten:
            print("cf win!")
            break



if __name__ == "__main__":
    main()
