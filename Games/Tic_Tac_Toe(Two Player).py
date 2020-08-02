import sys

po = [" "] * 9


def create_board():
    print("\n")
    print(po[0] + "  | " + po[1] + " | " + po[2])
    print(" - " + "+" + " - " + "+" + " - ")
    print(po[3] + "  | " + po[4] + " | " + po[5])
    print(" - " + "+" + " - " + "+" + " - ")
    print(po[6] + "  | " + po[7] + " | " + po[8])
    print("\n")


def isWin(po, le):
    if po[0] == po[1] == po[2] == le:  # The top row
        return True

    if po[0] == po[3] == po[6] == le:  # The first column
        return True

    if po[0] == po[4] == po[8] == le:  # The diagonal from top-left to bottom-right
        return True

    if po[2] == po[4] == po[6] == le:
        return True

    if po[2] == po[5] == po[8] == le:  # The last column
        return True

    if po[1] == po[4] == po[7] == le:  # The middle column
        return True

    if po[3] == po[4] == po[5] == le:  # The middle row
        return True

    if po[6] == po[7] == po[8] == le:  # The bottom row
        return True


def player1_move():
    print("\n")
    print("PLAYER 1 TURN")
    print("\n")
    create_board()
    player_place = int(input("Where do you want to put the marker?: "))
    if " " not in po:
        pass
    elif po[player_place - 1] != " ":
        print("Space already occupied")
        player1_move()
    else:
        po[player_place - 1] = "X"
        if isWin(po, "X"):
            print("\n")
            print("PLAYER 1 WINS!!!")
            create_board()
            sys.exit()


def player2_move():
    print("\n")
    print("PLAYER 2 TURN")
    print("\n")
    create_board()
    player_place = int(input("Where do you want to put the marker?: "))

    if " " not in po:
        pass
    elif po[player_place - 1] != " ":
        print("Space already occupied")
        player2_move()
    else:
        po[player_place - 1] = "O"
        if isWin(po, "O"):
            print("\n")
            print("PLAYER 2 WINS!!!")
            create_board()
            sys.exit()


while " " in po:
    player1_move()
    player2_move()

create_board()
print("\n")
print("IT'S A DRAW!!!")