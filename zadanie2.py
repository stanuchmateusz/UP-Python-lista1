from random import choice


class Coin:
    def __init__(self) -> None:
        self._side = None

    def throw(self) -> None:
        self._side = choice(["orzel", "reszka"])

    def show_side(self) -> str:
        return self._side


def gra():
    saldo = 0
    while saldo < 20:
        for _ in range(3):
            coins = [Coin() for _ in range(3)]
            for coin in coins:
                coin.throw()
                if coin.show_side() == "orzel":
                    if coins.index(coin) == 0:
                        saldo += 1
                    elif coins.index(coin) == 1:
                        saldo += 2
                    else:
                        saldo += 5
                # print(coin.show_side())

    print(f"Saldo końcowe: {saldo}")
    if saldo == 20:
        return True
    return False


if __name__ == "__main__":
    wygrane = 0
    przegrane = 0
    for x in range(1000):
        print(f"Gra nr:{x} ", end="")
        if(gra()):
            wygrane += 1
        else:
            przegrane += 1

    print(f"Wygrane: {wygrane} Przegrane: {przegrane}")
