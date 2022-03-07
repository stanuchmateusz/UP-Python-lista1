# brak implementacji ale klasa wygląda poprawnie


class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False) -> None:
        self.count += 1
        self._name = name
        self._power = power
        self._working = working

    def start(self):
        if not self._working:
            self.all_power += self._power
            self._working = True

    def stop(self):
        if self._working:
            self.all_power -= self._power
            self._working = False

    def __str__(self):
        return f"{self._name} {self._power} {self._working}"

    def __del__(self):
        self.count -= 1

    def status(self):
        print(f"{self._name} {self._power} {self._working}")
