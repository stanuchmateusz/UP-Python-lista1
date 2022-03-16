import random

from numpy import void


class minesweeper:
    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.mines_number = None
        self.mines = []
        self.board = None

    def get_numer(self, a, b, text) -> int:
        liczba = 0
        while liczba < a or liczba > b:
            try:
                liczba = int(
                    input(f"{text} od {a} do {b}\n"))
                if liczba < a or liczba > b:
                    raise ValueError
                else:
                    return liczba
            except(ValueError):
                print("Podana wartość nie jest liczbą całkowitą z podanego zakresu")

    def lay_mines(self) -> list:
        if self.x == None or self.y == None or self.mines_number == None:
            raise ValueError("Nie ustawiono wymiarów planszy lub liczby min")

        mines = []
        for _ in range(self.mines_number):
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            if (x, y) not in self.mines:
                mines.append((x, y))

        return mines

    def number_of_neighbouring_mines(self, field) -> int:
        if self.mines is None:
            raise ValueError("Nie ustawiono min")
        x, y = field
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x + i, y + j) in self.mines:
                    neighbours += 1
        return neighbours

    def create_board(self) -> list:
        if self.x is None or self.y is None:
            raise ValueError("Nie ustawiono wymiarów planszy")

        board = []
        for i in range(self.y):
            board.append([])
            for j in range(self.x):
                if (i, j) in self.mines:
                    board[i].append(9)
                else:
                    board[i].append(self.number_of_neighbouring_mines((i, j)))
        return board

    def reveal_field(self, field, b) -> int:  # trochę działa
        x, y = field

        if x < 0 or x > self.x - 1 or y < 0 or y > self.y - 1:
            return 0

        if b[x][y] == 10:
            return 1

        if field in self.mines:
            b[x][y] = 9
            return -1
        if self.board[x][y] == 0:
            b[x][y] = 10
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.reveal_field((x+i, y+j), b)
        else:
            b[x][y] = self.board[x][y]

        return 1

    def print_board(self, board) -> void:
        if board is None:
            raise ValueError("Nie ustawiono planszy")

        # góra
        print("")
        print(chr(9553), end="")
        for i in range(self.x):
            print(i, end="|")
        print(chr(9553))  # ╔

        print(chr(9567), end="")
        for _ in range(len(board[0])*2):
            print(chr(9472), end="")
        print(chr(9570))

        # treść
        for i in range(len(board)):
            print(chr(9553), end="")
            for j in board[i]:
                if j == 9:
                    print("\33[31m*\033[0m", end=".")
                elif j == 0:
                    print("O", end=".")
                elif j == 10:
                    print(" ", end=".")
                else:
                    print(f'\33[{40+j}m{j}\033[0m', end=".")
            print(chr(9553), i)

        # góra
        print(chr(9562), end="")
        for _ in range(len(board[0])*2):
            print(chr(9552), end="")
        print(chr(9565))
