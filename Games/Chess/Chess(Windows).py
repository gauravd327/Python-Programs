import pygame
import time
import sys

pygame.init()

# Initializing game window
screen_width = 600
cell_size = (screen_width) // 8
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

copy = gameboard
undolist, redolist = [], []

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
for x in range(6):
    white[x] = pygame.transform.scale(white[x], (cell_size, cell_size))
    black[x] = pygame.transform.scale(black[x], (cell_size, cell_size))

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
def getMoves(board):
    global counter
    pawnlist, rooklist = [], []
    knightlist, bishoplist = [], []
    kinglist, queenlist = [], []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
                if gameboard[i][j] * counter <= 1:
                    if abs(gameboard[i][j]) == 1:
                        for x in pawncheck.validList(board, 1 * gameboard[i][j], i, j):
                            pawnlist.append(x)

                    elif abs(gameboard[i][j]) == 2:
                        for x in rookcheck.validList(board, 2 * gameboard[i][j], i, j):
                            rooklist.append(x)
                        

                    elif abs(gameboard[i][j]) == 3:
                            for x in knightcheck.validList(board, 3 * gameboard[i][j], i, j):
                                knightlist.append(x)
                        

                    elif abs(gameboard[i][j]) == 4:
                        for x in bishopcheck.validList(board, 4 * gameboard[i][j], i, j):
                            bishoplist.append(x)   
                        

                    elif abs(gameboard[i][j]) == 5:
                        for x in kingcheck.validList(board, 5 * gameboard[i][j], i, j):
                            kinglist.append(x)
                        

                    elif abs(gameboard[i][j]) == 6:
                        for x in (rookcheck.validList(board, 2 * gameboard[i][j], i, j) + bishopcheck.validList(board, 4 * gameboard[i][j], i, j)):
                            queenlist.append(x)
                    

    gamelist = [pawnlist, rooklist, knightlist, bishoplist, kinglist, queenlist]
    #print("\n" * 2)
    #print("Pawn: ", pawnlist)
    #print("Rook: : ", rooklist)
    #print("Knight: ", knightlist)
    #print("Bishop: ", bishoplist)
    #print("King: ", kinglist)
    #print("Queen: ", queenlist)
    #print("\n" * 2)
    return gamelist


def check(gamelist):
    for i in range(len(gamelist)):
        for j in range(len(gamelist[i])):
            #print(gamelist[i][j], white_king, black_king, i)
            if gamelist[i][j] == white_king:
                print("White king is in Check")  
                print("\n")
                return 1

            elif gamelist[i][j] == black_king:
                print("Black King is in Check")
                print("\n")
                return -1

    return False      

def isValid(board, piece, y, x, oldy, oldx):
    global pawncheck, rookcheck, knightcheck, bishopcheck, kingcheck
    result = []

    total = [pawncheck.validList(board, piece, oldx, oldy),
             rookcheck.validList(board, piece, oldx, oldy),
             knightcheck.validList(board, piece, oldx, oldy),
             bishopcheck.validList(board, piece, oldx, oldy),
             kingcheck.validList(board, piece, oldx, oldy),
             rookcheck.validList(board, piece,  oldx, oldy) + bishopcheck.validList(board, piece, oldx, oldy)]

    result = total[abs(piece) - 1]
    
    
    if result is None:
        return False


    elif [y, x] in result:
        

        if abs(x - oldy) > 1 and abs(piece) == 5:
            if x - oldy == 2:
                board[y][x - 1] = 2 * (piece // abs(piece))
                board[y][x + 1] = 0
                

            elif oldy - x == 3:
                board[y][x - 2] = 0
                board[y][x + 1] = 2 * (piece // abs(piece))


        return True

    
    return False


global counter
counter = 1
# Creating a "Piece" class that defines the basic functionality of a piece
class Piece:

    # Moving a piece that has been clicked on
    def move(self, board, selected_piece, piece, ypos, xpos):
        
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


        

class Pawn(Piece):

    def validList(self, board, piece, y, x):
        try:
            if gameboard[y][x] < 0:
                temp = y + 1

            else:
                temp = y - 1

            poslist = []
            start = 1

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if y == 1 or y == 6:
                        start = 2

                    else:
                        start = 1
                    if 0 <= abs(y - i) <= start and abs(j - x) <= 0:
                        if y > i and piece == 1:
                            if (board[i][j] * piece) <= 0:
                                poslist.append([i, j])

                        elif y < i and piece == -1:
                            if (board[i][j] * piece) <= 0:
                                poslist.append([i, j])

                        

            if board[temp][x - 1] != 0:
                poslist.append([temp, x - 1])


            if board[temp][x + 1] != 0:
                poslist.append([temp, x + 1])

        except:
            pass


        return poslist

class Rook(Piece):

    def validList(self, board, piece, y, x):
        poslist = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                valid = True
                z, new_y, new_x = 1, 0, 0
                if i == y or j == x:
                    while z < max(abs(x - j), abs(y - i)):
                        if i == y:
                            if j > x:
                                new_y, new_x = y, j - z


                            elif j < x:
                                new_y, new_x = y, (j + abs(x - j)) - z

                        elif j == x:
                            if i > y:
                                new_y, new_x = i - z, x


                            elif i < y:
                                new_y, new_x = (i + abs(y - i)) - z, x

                        if board[new_y][new_x] != 0:
                            valid = False
                            break


                        z += 1
                    if valid:
                        if (board[i][j] * piece) <= 0:
                            poslist.append([i, j])

        return poslist


class Bishop(Piece):

    def validList(self, board, piece, y, x):
        poslist = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                valid = True
                z, new_y, new_x = 1, 0, 0

                if abs(i - y) == abs(j - x):
                    while z < abs(x - j):
                        if i > y:
                            if j > x:
                                new_y, new_x = y + z, x + z


                            elif j < x:
                                new_y, new_x = y + z, x - z

                        elif i < y:
                                if j > x:
                                    new_y, new_x = y - z, x + z


                                elif j < x:
                                    new_y, new_x = y - z, x - z

                        if board[new_y][new_x] != 0:
                            valid = False
                            break


                        z += 1

                    if valid:
                        if (board[i][j] * piece) <= 0:
                            poslist.append([i, j])

        return poslist


class Knight(Piece):

    def validList(self, board, piece, y, x):
        poslist = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (abs(i - y) == 1 and abs(j - x) == 2):
                    if (board[i][j] * piece) <= 0:
                        poslist.append([i, j])

                elif (abs(i - y) == 2 and abs(j - x) == 1):
                    if (board[i][j] * piece) <= 0:
                        poslist.append([i, j])

        return poslist


class King(Piece):


    def validList(self, board, piece, y, x):
        try:
            poslist = []
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if abs(i - y) <= 1 and abs(j - x) <= 1:
                        if (board[i][j] * piece) <= 0:
                            poslist.append([i, j])

            if x == 4 and abs(board[y][x]) == 5:
                if board[y][x + 1] == 0 and board[y][x + 2] == 0:
                    poslist.append([y, x + 2])

                if board[y][x - 1] == 0 and board[y][x - 2] == 0 and board[y][x - 3] == 0:
                    poslist.append([y, x - 2])


            return poslist

        except:
            pass

def equalize(list1, list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            list2[i][j] = list1[i][j]

def placeMove(board, curr_piece, val, curr_y, curr_x, pos2, pos1):
    global counter

    board[pos2][pos1], board[curr_y][curr_x] = 0, board[pos2][pos1]
    result = check(getMoves(board))
                            
    if (counter * result) >= 1:
        board[curr_y][curr_x] = val
        board[pos2][pos1] = curr_piece
        return False

    return True
            





# Gameloop

flip = True
rookcheck = Rook()
bishopcheck = Bishop()
knightcheck = Knight()
kingcheck = King()
pawncheck = Pawn()

def main():
    crashed = False
    clock = pygame.time.Clock() 
    selected = None
    pos1, pos2 = 0, 0
    curr_piece = 0

    global gameboard, counter, flip, white_king, black_king

    while not crashed:
        common = Piece()
        
        # Checking if a piece is being hovered over
        curr_x, curr_y = pygame.mouse.get_pos()
        piece, x, y = hover()   
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                crashed = True

            state = pygame.key.get_pressed()
            if state[pygame.K_UP]:
                flipBoard(gameboard)

            if state[pygame.K_f]:
                if flip:
                    flip = False

                else:
                    flip = True

            if state[pygame.K_r]:
                counter = 1
                gameboard = [[-2, -3, -4, -6, -5, -4, -3, -2],
                             [-1, -1, -1, -1, -1, -1, -1, -1],
                             [ 0,  0,  0,  0,  0,  0,  0,  0],
                             [ 0,  0,  0,  0,  0,  0,  0,  0],
                             [ 0,  0,  0,  0,  0,  0,  0,  0],
                             [ 0,  0,  0,  0,  0,  0,  0,  0],
                             [ 1,  1,  1,  1,  1,  1,  1,  1],
                             [ 2,  3,  4,  6,  5,  4,  3,  2]]


            if state[pygame.K_LEFT]:
                try:
                    equalize(undolist[-1], gameboard)
                    redolist.append(gameboard)
                    undolist.pop()
                except:
                    pass


            if state[pygame.K_RIGHT]:
                try:
                    gameboard = redolist[-1]
                    undolist.append(gameboard)
                    redolist.pop()
                except:
                    pass
  
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

                gameboard[pos2][pos1] = curr_piece
                curr_x //= cell_size
                curr_y //= cell_size

                

                # Swapping positions with the desired location
                if isValid(gameboard, curr_piece, curr_y, curr_x, pos1, pos2) and (gameboard[curr_y][curr_x] * gameboard[pos2][pos1]) <= 0 and (curr_piece * counter >= 0):
                    
                    if curr_x != pos1 or curr_y != pos2:
                        if gameboard[pos2][pos1] == 5:
                            white_king = [curr_y, curr_x]
                        
                        elif gameboard[pos2][pos1] == -5:
                            black_king = [curr_y, curr_x]

                        if not placeMove(gameboard, curr_piece, gameboard[curr_y][curr_x], curr_y, curr_x, pos2, pos1):
                            counter *= -1
                        

                        undolist.append(gameboard)
                        
                        print(white_king, black_king, counter)
                        if flip:
                            time.sleep(0.05)
                            #flipBoard(gameboard)

                        
                        
                        counter *= -1

        displayBoard(gameboard)
        common.move(gameboard, selected, curr_piece, pos1, pos2)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

