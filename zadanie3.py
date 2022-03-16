from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = randint(1, self.sides)

    def get_sides(self):
        return self.sides

    def get_value(self):
        return self.value


def gra():
    suma_gracz = 0
    suma_komputer = 0

    while suma_komputer < 20 or suma_gracz < 20:
        wybor = input("Czy chcesz kontynułować grę? (t/n)")
        if wybor == "n":
            break

        kostka = Die()
        kostka.roll()
        suma_gracz += kostka.get_value()
        print(f"Suma oczek gracza: {suma_gracz}")
        kostka.roll()
        suma_komputer += kostka.get_value()

    print(f"Suma oczek komputera: {suma_komputer}")

    if suma_gracz > 21:
        return False
    if suma_komputer > 21:
        return True

    if suma_komputer < suma_gracz:
        return True
    return False


if __name__ == '__main__':
    if gra():
        print("Wygrałeś!")
    else:
        print("Przegrałeś!")
