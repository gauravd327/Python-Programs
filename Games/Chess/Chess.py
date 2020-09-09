import pygame
import sys
from pygame import mixer
from Pieces import Pawn, Rook, Knight, Bishop, King

pygame.init()
mixer.init()

mixer.music.load("Games\Chess\Chess_Move.wav")
mixer.music.set_volume(0.7)

# Initializing game window
screen_width = 600
cell_size = screen_width // 8
screen_height = screen_width

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess')

# Colors
RED = (255, 0, 0, 50)
GREEN = (0, 255, 0, 50)
BLUE = (0, 0, 255, 50)
WHITE = (255, 255, 255, 50)
BLACK = (0, 0, 0, 50)
YELLOW = (255, 255, 0, 50)

# The chess board(represented as an array)
gameboard = [[-2, -3, -4, -6, -5, -4, -3, -2], 
             [-1, -1, -1, -1, -1, -1, -1, -1], 
             [ 0,  0,  0,  0,  0,  0,  0,  0], 
             [ 0,  0,  0,  0,  0,  0,  0,  0], 
             [ 0,  0,  0,  0,  0,  0,  0,  0], 
             [ 0,  0,  0,  0,  0,  0,  0,  0], 
             [ 1,  1,  1,  1,  1,  1,  1,  1], 
             [ 2,  3,  4,  6,  5,  4,  3,  2]]

# Loading images
background = pygame.image.load("Games\Chess\Images\Chess_Board.png")

white = [pygame.image.load('Games\Chess\Images\White_Pieces\pawn_white.png'),
         pygame.image.load('Games\Chess\Images\White_Pieces\Rook_white.png'),
         pygame.image.load('Games\Chess\Images\White_Pieces\knight_white.png'),
         pygame.image.load('Games\Chess\Images\White_Pieces\Bishop_white.png'),
         pygame.image.load('Games\Chess\Images\White_Pieces\king_white.png'),
         pygame.image.load('Games\Chess\Images\White_Pieces\Queen_white.png')]

black = [pygame.image.load('Games\Chess\Images\Black_Pieces\pawn_black.png'),
         pygame.image.load('Games\Chess\Images\Black_Pieces\Rook_black.png'),
         pygame.image.load('Games\Chess\Images\Black_Pieces\knight_black.png'),
         pygame.image.load('Games\Chess\Images\Black_Pieces\Bishop_black.png'),
         pygame.image.load('Games\Chess\Images\Black_Pieces\king_black.png'),
         pygame.image.load('Games\Chess\Images\Black_Pieces\queen_black.png')]

background = pygame.transform.scale(background, (screen_width, screen_height))

for z in range(6):
    white[z] = pygame.transform.scale(white[z], (cell_size, cell_size))
    black[z] = pygame.transform.scale(black[z], (cell_size, cell_size))

white_king = [7, 4]
black_king = [0, 4]


# Displaying the Chess Board
def displayBoard(board):
    win.blit(background, (0, 0))
    global white_king, black_king
    hover()

    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] >= 1:
                win.blit(white[board[i][j] - 1], (j * cell_size, i * cell_size))

            elif board[i][j] <= -1:
                win.blit(black[abs(board[i][j]) - 1], (j * cell_size, i * cell_size))


def flipBoard(board):
    size = len(board)
    for i in range(len(gameboard) // 2):
        for j in range(len(gameboard[i])):
            gameboard[i][j], gameboard[size - i - 1][j] = gameboard[size - i - 1][j], gameboard[i][j]


# Creating a "yellow" outline if a cell/square is hovered over
def hover():
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            curr_x = pygame.mouse.get_pos()[0] // cell_size
            curr_y = pygame.mouse.get_pos()[1] // cell_size
            if curr_x <= 7 and curr_y <= 7:
                pygame.draw.rect(win, YELLOW, (curr_x * cell_size, curr_y * cell_size, cell_size, cell_size), 4)

                # Returning x, y coordinates and the type of piece
                # if the mouse is hovering over an occupied cell

                if gameboard[curr_y][curr_x] != 0:
                    return gameboard[curr_y][curr_x], curr_x, curr_y

                return 0, curr_x, curr_y


def getMoves(piece, board):
    global counter
    pawnlist, rooklist = [], []
    knightlist, bishoplist = [], []
    kinglist, queenlist = [], []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if abs(gameboard[i][j]) == 1:
                for x in pawncheck.validList(board, 1 * gameboard[i][j], i, j):
                    pawnlist.append(x + [i, j, gameboard[i][j]])

            elif abs(gameboard[i][j]) == 2:
                for x in rookcheck.validList(board, 2 * gameboard[i][j], i, j):
                    rooklist.append(x + [i, j, gameboard[i][j]])

            elif abs(gameboard[i][j]) == 3:
                for x in knightcheck.validList(board, 3 * gameboard[i][j], i, j):
                    knightlist.append(x + [i, j, gameboard[i][j]])

            elif abs(gameboard[i][j]) == 4:
                for x in bishopcheck.validList(board, 4 * gameboard[i][j], i, j):
                    bishoplist.append(x + [i, j, gameboard[i][j]])

            elif abs(gameboard[i][j]) == 5:
                for x in kingcheck.validList(board, 5 * gameboard[i][j], i, j):
                    kinglist.append(x + [i, j, gameboard[i][j]])

            elif abs(gameboard[i][j]) == 6:
                for x in (rookcheck.validList(board, 2 * gameboard[i][j], i, j) + bishopcheck.validList(board, 4 * gameboard[i][j], i, j)):
                    queenlist.append(x + [i, j, gameboard[i][j]])

    gamelist = [pawnlist, rooklist, knightlist, bishoplist, kinglist, queenlist]

    return gamelist


# Moving a piece that has been clicked on
def move(board, selected_piece, piece, ypos, xpos):
    if selected_piece:

        # Drawing a green square around the selected piece
        if xpos is not None:
            rect = (ypos * cell_size, xpos * cell_size, cell_size, cell_size)
            pygame.draw.rect(win, GREEN, rect, 4)

        pos = pygame.mouse.get_pos()

        # Checking if the piece is white or black
        if piece > 0:
            win.blit(white[piece - 1], white[board[xpos][ypos] - 1].get_rect(center=pos))

        elif piece < 0:
            win.blit(black[abs(piece) - 1], black[abs(board[xpos][ypos]) - 1].get_rect(center=pos))

    return





def isValid(board, piece, y, x, oldy, oldx):
    global pawncheck, rookcheck, knightcheck, bishopcheck, kingcheck
    result = []

    total = [pawncheck.validList(board, piece, oldx, oldy),
             rookcheck.validList(board, piece, oldx, oldy),
             knightcheck.validList(board, piece, oldx, oldy),
             bishopcheck.validList(board, piece, oldx, oldy),
             kingcheck.validList(board, piece, oldx, oldy),
             rookcheck.validList(board, piece, oldx, oldy) + bishopcheck.validList(board, piece, oldx, oldy)]

    result = total[abs(piece) - 1]

    if result is None:
        return False

    elif [y, x] in result:
        return True

    return False


global counter
counter = 1

def checkmate(piece, board):
    global counter
    
    
    checklist = []
    for i in range(len(getMoves(piece, board))):
        for j in getMoves(piece, board)[i]:
            if (j[0] >= 0) and (j[1] >= 0) and (j[2] >= 0) and (j[3] >= 0):

                result = placeMove(board, j[4], board[j[0]][j[1]], j[0], j[1], j[2], j[3])
                if result is True:
                    checklist.append(j)
                
                else:
                    pass
  
    
   
    return checklist

def check(gamelist):
    for i in range(len(gamelist)):
        for j in range(len(gamelist[i])):
            if gamelist[i][j][0:2] == white_king:
                return 1

            elif gamelist[i][j][0:2] == black_king:

                return -1

    return None

def placeMove(board, curr_piece, val, curr_y, curr_x, pos2, pos1): 
    global counter, white_king, black_king

    board[curr_y][curr_x] = board[pos2][pos1]
    board[pos2][pos1] = 0

    if gameboard[curr_y][curr_x] == -5:
        black_king = [curr_y, curr_x]

    if gameboard[curr_y][curr_x] == 5:
        white_king = [curr_y, curr_x]

    result = check(getMoves(curr_piece, board))
    
    if gameboard[curr_y][curr_x] == -5:
        black_king = [pos2, pos1]

    if gameboard[curr_y][curr_x] == 5:
        white_king = [pos2, pos1]

    board[curr_y][curr_x] = val
    board[pos2][pos1] = curr_piece

    
    if result and result * curr_piece > 0: 
        return False

    else:
        return True


def castle(y, x, oldx, piece, board):
    if x - oldx == 2:
        board[y][x - 1] = 2 * (piece // abs(piece))
        board[y][x - 4] = 0

    elif oldx - x == 2:
        board[y][x + 1] = 2 * (piece // abs(piece))
        board[y][x + 3] = 0


# Gameloop

rookcheck = Rook()
bishopcheck = Bishop()
knightcheck = Knight()
kingcheck = King()
pawncheck = Pawn()


def main():
    crashed = False
    clock = pygame.time.Clock()
    selected = None
    pos1, pos2 = None, None
    curr_piece = 0
    incheck = False

    global gameboard, counter, white_king, black_king

    while not crashed:
        displayBoard(gameboard)

        # Checking if a piece is being hovered over
        curr_x, curr_y = pygame.mouse.get_pos()
        piece, x, y = hover()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True

            state = pygame.key.get_pressed()
            if state[pygame.K_UP]:
                flipBoard(gameboard)

            if state[pygame.K_r]:
                counter = 1
                gameboard = [[-2, -3, -4, -6, -5, -4, -3, -2],
                             [-1, -1, -1, -1, -1, -1, -1, -1],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [1, 1, 1, 1, 1, 1, 1, 1],
                             [2, 3, 4, 6, 5, 4, 3, 2]]

            # Drag and drop functionality(If the mousebutton is pressed)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Saving the x, y coordinates and the type of piece
                
                selected = True
                pos1, pos2 = x, y
                gameboard[pos2][pos1] = 0
                curr_piece = piece

            # Drag and drop functionality(If the mousebutton is lifted)
            if event.type == pygame.MOUSEBUTTONUP:
                
                selected = None
                try:
                    gameboard[pos2][pos1] = curr_piece
                    curr_x //= cell_size
                    curr_y //= cell_size

                except:
                    pass

                # Swapping positions with the desired location
                if isValid(gameboard, curr_piece, curr_y, curr_x, pos1, pos2) and (gameboard[curr_y][curr_x] * gameboard[pos2][pos1]) <= 0 and (curr_piece * counter >= 0):
                    if curr_x != pos1 or curr_y != pos2:
                        if gameboard[pos2][pos1] == 5:
                            white_king = [curr_y, curr_x]

                        elif gameboard[pos2][pos1] == -5:
                            black_king = [curr_y, curr_x]

                        result = checkmate(curr_piece, gameboard)
                        

                        if [curr_y, curr_x, pos2, pos1, curr_piece] not in result:
                            
                            if not placeMove(gameboard, curr_piece, gameboard[curr_y][curr_x], curr_y, curr_x, pos2, pos1): 
                                counter = curr_piece // abs(curr_piece)


                            counter *= -1 

                        else:
                            mixer.music.play()
                            if placeMove(gameboard, curr_piece, gameboard[curr_y][curr_x], curr_y, curr_x, pos2, pos1):
                                gameboard[pos2][pos1], gameboard[curr_y][curr_x] = 0, gameboard[pos2][pos1]

                                if abs(gameboard[curr_y][curr_x]) == 5:
                                    castle(pos2, pos1, curr_x, curr_piece, gameboard)

                                       
                        final = checkmate(curr_piece, gameboard)
                        negative, positive = 0, 0
                        for i in final:

                            if i[4] < 0:
                                negative += 1

                            else:
                                positive += 1


                        if negative * positive <= 0:
                            print("CHECKMATE")

                            sys.exit()

                    counter *= -1

        if check(getMoves(curr_piece, gameboard)):
            if check(getMoves(piece, gameboard)) == 1:
                rect = (white_king[1] * cell_size, white_king[0] * cell_size, cell_size, cell_size)
                pygame.draw.rect(win, RED, rect, 4)

            elif check(getMoves(piece, gameboard)) == -1:
                rect = (black_king[1] * cell_size, black_king[0] * cell_size, cell_size, cell_size)
                pygame.draw.rect(win, RED, rect, 4)

        move(gameboard, selected, curr_piece, pos1, pos2)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
