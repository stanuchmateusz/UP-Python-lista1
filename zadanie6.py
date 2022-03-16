# brak implementacji ale klasa wygląda poprawnie


class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False) -> None:
        RocketEngine.count += 1
        self._name = name
        self._power = power
        self._working = working

    def start(self):
        if not self._working:
            RocketEngine.all_power += self._power
            self._working = True

    def stop(self):
        if self._working:
            RocketEngine.all_power -= self._power
            self._working = False

    def __str__(self):
        return f"{self._name} {self._power} {self._working}"

    def __del__(self):
        RocketEngine.count -= 1

    @staticmethod
    def status():
        print(f" moc {__class__.all_power} ilość {RocketEngine.count}")


def main():
    silniki = [
        RocketEngine("Pierwszy", 50), RocketEngine("Drugi", 50), RocketEngine("Trzeci", 500), RocketEngine(
            "Czwarty", 500), RocketEngine("Piąty", 40000), RocketEngine("Szósty", 400000)
    ]
    for silnik in silniki:
        silnik.start()
        print(silnik)

    RocketEngine.status()


if __name__ == '__main__':
    main()
