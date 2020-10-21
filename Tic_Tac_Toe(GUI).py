import pygame
from sys import exit
from time import sleep


pygame.init()


screen_width = 600
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

running = True

gamboard = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def createBoard():
    x, y = screen_width // 120, screen_height // 120
    cell_width = (screen_width - x * 2) // 3
    cell_height = (screen_height - x * 2) // 3

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(win, (255, 255, 255), (x, y, cell_width - 5, cell_height - 5))
            x += (screen_width // 3)

        x = screen_width // 120
        y += (screen_height // 3)
        
def drawBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                pygame.draw.line(win, (0, 0, 0), (((i * 200) + 50), ((j * 200) + 50)), (((i * 200) + 150), ((j * 200) + 150)), 15)
                pygame.draw.line(win, (0, 0, 0), (((i * 200) + 150), ((j * 200) + 50)), (((i * 200) + 50), ((j * 200) + 150)), 15)

            elif board[i][j] == "O":
                pygame.draw.circle(win, (0, 0, 0), ((i * 200) + 100, (j * 200) + 100), screen_height // 9)
                pygame.draw.circle(win, (255, 255, 255), ((i * 200) + 100, (j * 200) + 100), screen_height // 11)


def getMousePos():
    x, y = pygame.mouse.get_pos()

    x = x // (screen_width // 3)
    y = y // (screen_height // 3)

    return (x, y)


def placeMarker(i, j, marker, board):
    if board[i][j] == " ":
        board[i][j] = marker
        return True

    return False

def checkWinner(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
                return True

            elif board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
                return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        return True

    

    return False


def main():

    global running
    counter = 1  
    gameover = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    

            if event.type == pygame.MOUSEBUTTONDOWN:
                result = getMousePos()

                if(counter % 2 == 1):
                    if placeMarker(result[0], result[1], "X", gamboard):
                        counter += 1

                else:
                    if placeMarker(result[0], result[1], "O", gamboard):
                        counter += 1


        if counter >= 10:
            gameover = True

        elif checkWinner(gamboard):
            if (counter % 2) == 0:
                print("\nX is the winner!\n")


            else:
                print("\nO is the winner\n")


            gameover = True


        win.fill((0, 0, 0))
        createBoard()
        drawBoard(gamboard)

        if(gameover):                
            running = False
            drawBoard(gamboard) 


        pygame.display.update()

    pygame.quit()
    

if __name__ == "__main__":
    main()
   