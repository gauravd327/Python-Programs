import pygame
pygame.init()

# Initializing game window
screen_width = 600
screen_height = 600

cell_size = (screen_height + screen_width) // 16

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
             [ 0,  0,  0,  0,  0,  1,  0,  0],
             [ 0,  0,  0,  0,  4,  0,  0,  0],
             [ 0,  0,  0,  0,  0,  0,  0,  0],
             [ 0,  0,  1,  0,  0,  0,  1,  0],
             [ 1,  1,  1,  1,  1,  1,  1,  1],
             [ 2,  3,  4,  6,  5,  4,  3,  2]]

# Loading images
background = pygame.image.load('Chess\Images\Chess_Board.png')

white = [pygame.image.load('Chess\Images\White_Pieces\pawn_white.png'),
         pygame.image.load('Chess\Images\White_Pieces\Rook_white.png'),
         pygame.image.load('Chess\Images\White_Pieces\knight_white.png'),
         pygame.image.load('Chess\Images\White_Pieces\Bishop_white.png'),
         pygame.image.load('Chess\Images\White_Pieces\king_white.png'),
         pygame.image.load('Chess\Images\White_Pieces\Queen_white.png')]

black = [pygame.image.load('Chess\Images\Black_Pieces\pawn_black.png'),
         pygame.image.load('Chess\Images\Black_Pieces\Rook_black.png'),
         pygame.image.load('Chess\Images\Black_Pieces\knight_black.png'),
         pygame.image.load('Chess\Images\Black_Pieces\Bishop_black.png'),
         pygame.image.load('Chess\Images\Black_Pieces\king_black.png'),
         pygame.image.load('Chess\Images\Black_Pieces\queen_black.png')]


# Displaying the Chess Board
def displayBoard():
    win.blit(background, (0, 0))
    hover()

    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][j] >= 1:
                win.blit(white[gameboard[i][j] - 1], (j * cell_size, i * cell_size))

            elif gameboard[i][j] <= -1:
                win.blit(black[abs(gameboard[i][j]) - 1], (j * cell_size, i * cell_size))

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
            pygame.draw.rect(win, YELLOW, (curr_x * cell_size, curr_y * cell_size, cell_size, cell_size), 4)

            # Returning x, y coordinates and the type of piece
            # if the mouse is hovering over an occupied cell

            if gameboard[curr_y][curr_x] != 0:
                return gameboard[curr_y][curr_x], curr_x, curr_y

            return 0, curr_x, curr_y


def isValid(piece, y, x, oldy, oldx):
    rookcheck = Rook()
    bishopcheck = Bishop()
    knightcheck = Knight()
    kingcheck = King()
    pawncheck = Pawn()
    result = []

    if abs(piece) == 1:
        result = pawncheck.validList(oldx, oldy)


    if abs(piece) == 2:
        result = rookcheck.validList(oldx, oldy)

    elif abs(piece) == 3:
        result = knightcheck.validList(oldx, oldy)

   
    elif abs(piece) == 4:
        result = bishopcheck.validList(oldx, oldy)
        print(result)

    elif abs(piece) == 5:
        result = kingcheck.validList(oldx, oldy)


    elif abs(piece) == 6:
        result = rookcheck.validList(oldx, oldy) + bishopcheck.validList(oldx, oldy)


    if result is None:
        return False


    elif [y, x] in result:
            return True


    return False

# Creating a "Piece" class that defines the basic functionality of a piece
class Piece:

    # Moving a piece that has been clicked on
    def move(self, selected_piece, piece, ypos, xpos):
        if selected_piece:

            # Drawing a green square around the selected piece
            if xpos is not None:
                rect = (ypos * cell_size, xpos * cell_size, cell_size, cell_size)
                pygame.draw.rect(win, GREEN, rect, 4)

            pos = pygame.mouse.get_pos()

            # Checking if the piece is white or black
            if piece > 0:
                win.blit(white[piece - 1], white[gameboard[xpos][ypos] - 1].get_rect(center=pos))


            elif piece < 0:
                win.blit(black[abs(piece) - 1], black[abs(gameboard[xpos][ypos]) - 1].get_rect(center=pos))

        return

class Pawn(Piece):

    def validList(self, y, x):
        poslist = []
        start = 1
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if y == 1 or y == 6:
                    start = 2
 
                else:
                    start = 1
                if 0 <= abs(i - y) <= start and abs(j - x) <= 1:

                    poslist.append([i, j])

        return poslist

class Rook(Piece):

    def validList(self, y, x):
        poslist = []
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                valid = True
                z = 1
                if i == y:               
                    while z < abs(x - j):
                        if j > x:
                            if gameboard[y][j - z] != 0:
                                valid = False
                                break
                            
                        elif j < x:
                            print(2, [i, j, y, x, abs(x - j)])
                            if gameboard[y][(j + abs(x - j))- z] != 0:
                                valid = False
                                break
                            
                        z += 1
                    if valid:
                        poslist.append([i, j])    

                elif j == x:
                    while z < abs(y - i):
                        if i > y:
                            if gameboard[i - z][x] != 0:
                                valid = False
                                break
                            
                        elif i < y:
                            if gameboard[(i + abs(y - i))- z][x] != 0:
                                valid = False
                                break
                            
                        z += 1
                    if valid:
                        poslist.append([i, j])   

                    
                             
        return poslist

class Knight(Piece):

    def validList(self, y, x):
        poslist = []
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if (abs(i - y) == 1 and abs(j - x) == 2) or (abs(i - y) == 2 and abs(j - x) == 1):
                    poslist.append([i, j])

        return poslist

class Bishop(Piece):

    def validList(self, y, x):
        poslist = []
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                valid = True
                if i > y:  
                    z = 1              
                    while z < abs(x - j):
                        if j > x:
                            print(4, [i, j, y, x, abs(x - j)])
                            if gameboard[y - z][j - z] != 0:
                                valid = False
                                break
                            
                        elif j < x:
                            print(3, [i, j, y, x, abs(x - j)])
                            if gameboard[y - z][j + z] != 0:
                                valid = False
                                break
                            
                        z += 1
                    if valid:
                        poslist.append([i, j])    

                 

        return poslist

class King(Piece):

    def validList(self, y, x):
        poslist = []
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if abs(i - y) <= 1 and abs(j - x) <= 1:
                    
                    poslist.append([i, j])

        return poslist


# Gameloop
def main():
    # Gameloop variables

    crashed = False
    clock = pygame.time.Clock()
    selected = None
    pos1, pos2 = 0, 0
    curr_piece = 0

    while not crashed:
        common = Rook()

        # Checking if a piece is being hovered over
        curr_x, curr_y = pygame.mouse.get_pos()
        piece, x, y = hover()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                crashed = True

            state = pygame.key.get_pressed()
            if state[pygame.K_f]:
                flipBoard(gameboard)


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

                curr_x //= cell_size
                curr_y //= cell_size

                isValid(curr_piece, curr_x, curr_y, pos1, pos2)


                # Swapping positions with the desired location
                if isValid(curr_piece, curr_y, curr_x, pos1, pos2) and (gameboard[curr_y][curr_x] <= gameboard[pos2][pos1]):
                    if curr_x != pos1 or curr_y != pos2:
                        gameboard[pos2][pos1] = curr_piece
                        gameboard[pos2][pos1], gameboard[curr_y][curr_x] = 0, gameboard[pos2][pos1]

                    else:
                        gameboard[pos2][pos1] = curr_piece

                else:
                    gameboard[pos2][pos1] = curr_piece

        displayBoard()

        common.move(selected, curr_piece, pos1, pos2)

        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()