class Pet:
    def __init__(self, name) -> None:
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    def _passage_of_time(self) -> None:
        self.hunger += 1
        self.tiredness += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nazwa):
        if not nazwa or not nazwa.isalpha() or len(nazwa) < 3:
            raise ValueError("Podano nieprawidłową nazwę")
        self._name = nazwa

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, mood):
        if mood < 0:
            self._mood = 1
        elif mood > 4:
            self._mood = 4
        else:
            self._mood = mood

    def talk(self):
        s = self.hunger + self.tiredness
        if s < 5:
            self.mood = 0
        elif s < 10:
            self.mood = 1
        elif s < 15:
            self.mood = 2
        else:
            self.mood = 3
        self._passage_of_time()

        moods = ["szczęśliwy", "zadowolony", "podenerwowany", "wściekły"]
        print(f"{self.name} jest {moods[self._mood]}")

    def eat(self, food=4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._passage_of_time()

    def play(self, fun=4):
        self.tiredness -= fun
        if self.tiredness < 0:
            self.tiredness = 0
        self._passage_of_time()

    def __str__(self):
        return f"{self.name} | poziom glodu {self.hunger} | poziom znudzenia {self.tiredness}"


if __name__ == "__main__":

    pet = Pet(input("Wpisz nazwę swojego zwierzaka: "))
    while True:
        print("""
                      __
            \ ______/ V`-,
             }        /~~
            /_)^ --,r'
           |b      |b"`
           
        1. Porozmawiaj
        2. Nakarm
        3. Baw się
        4. Wyświetl stan zwierzaka (wpisz "xy")
        5. Wyjdź
        """)
        choice = input("Wybierz opcję: ")

        match choice:
            case "1":
                pet.talk()
            case "2":
                karma = input(
                    "Ile jedzenia chcesz dać pupilowi? (opcjonalne, domyślnie 4 porcje) ")
                if karma.isdigit():
                    pet.eat(int(karma))
                else:
                    pet.eat()
            case "3":
                czas = input(
                    "Ile czasu chcesz bawić się z pupilem? (opcjonalne, domyślnie 4 jednostki czasu) ")
                if czas.isdigit():
                    pet.play(int(czas))
                else:
                    pet.play()
            case "xy":
                print(pet)
            case "5":
                break
            case _:
                print("Nie ma takiej opcji")
