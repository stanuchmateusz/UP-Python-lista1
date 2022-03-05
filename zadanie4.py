class Account:
    def __init__(self, balance):
        self._balance = balance

    def pay(self, amount):
        self._balance += amount

    def take(self, amount):
        if (self._balance - amount) < 0:
            print("Brak środków na koncie")
            return
        self._balance -= amount

    def show_balance(self):
        return self._balance

    def __str__(self) -> str:
        return f"Stan konta: {self._balance}"


if __name__ == '__main__':
    account = Account(100)

    print(account)
    account.pay(10)
    print(account)
    account.take(50)
    print(account)
    account.take(200)
    print(account)
    account.pay(10)
    print(account)
