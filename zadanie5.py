import pickle
from random import randint


class Smartphone:
    def __init__(self, manufacturer, model, price):
        self._manufacturer = manufacturer
        self._model = model
        self._price = price

    def __str__(self):
        return f"Producent: {self._manufacturer}, Model: {self._model}, Cena: {self._price}"

# zepsute


with open("phones.dat", "w") as f:
    phones = [Smartphone("samsung", "model"+str(x), randint(100, 4300))
              for x in range(7)]
    for phone in phones:
        pickle.dump(obj=phone, file=f)

with open("phones.dat", "r") as f:
    print(pickle.load(f))
