from zadanie1_klasa import minesweeper


def saper():
    game = minesweeper()
    game.x = game.get_numer(8, 30, "Podaj wielkość planszy x z zakresu")
    game.y = game.get_numer(8, 24, "Podaj liczbę z zakresu y z zakresu")
    game.mines_number = game.get_numer(
        10, (game.x - 1) * (game.y - 1), "Podaj liczbę min z zakresu")

    # upewnienie się że pierwsze pole nie będzie minab
    while True:
        try:
            x, y = int(input("Podaj współrzędną x ")), int(
                input("Podaj współrzędną y "))
        except ValueError:
            print("Niepoprawna wartość")
            continue
        break

    game.mines = game.lay_mines()

    while (x, y) in game.mines:
        game.mines = game.lay_mines()
    # miny ułożono poprawnie

    # generowanie poprawnej planszy
    game.board = game.create_board()
    # game.print_board(game.board)

    # generowanie pustej planszy do wyświetlania
    playing_board = [([0] * game.y) for _ in range(game.x)]

    # umieszczenie pierwszego ruchu
    playing_board[x][y] = game.reveal_field((x, y), playing_board)

    game.print_board(playing_board)

    while True:
        try:
            y, x = int(input("Podaj współrzędną x ")), int(
                input("Podaj współrzędną y "))
        except ValueError:
            print("Niepoprawna wartość")
            continue
        print("")
        if(game.reveal_field((x, y), playing_board) == -1):
            game.print_board(playing_board)

            print("Koniec gry!")
            break

        if(not any(0 in r for r in playing_board)):
            game.print_board(playing_board)
            print("Wygrałeś!")
            break
        game.print_board(playing_board)


if __name__ == "__main__":
    try:
        saper()
    except EOFError:
        print("EOFError")
