import pickle
from random import randint


class Smartphone:
    def __init__(self, manufacturer, model, price):
        self._manufacturer = manufacturer
        self._model = model
        self._price = price

    def __str__(self):
        return f"Producent: {self._manufacturer}, Model: {self._model}, Cena: {self._price}"


with open("phones.dat", "wb") as file:
    phones = [str(Smartphone("samsung", "model"+str(x), randint(100, 4300)))
              for x in range(7)]
    pickle.dump(phones, file)

with open("phones.dat", "rb") as file:
    phones = pickle.load(file)
    for phone in phones:
        print(phone)
