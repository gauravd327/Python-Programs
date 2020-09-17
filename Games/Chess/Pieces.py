
class Pawn:

    def validList(self, board, piece, y, x):
        poslist = []
        try:
                
            if y == 1 or y == 6:
                start = 2

            else:
                start = 1

            if piece < 0:
                temp = y + start
                if start == 2:
                    if board[temp - 1][x] == 0:
                        poslist.append([temp - 1, x])

                if board[y + 1][x - 1] != 0:
                    poslist.append([y + 1, x - 1])

                if board[y + 1][x + 1] != 0:
                    poslist.append([y + 1, x + 1])

                
            else:
                temp = y - start
                if start == 2:
                    if board[temp + 1][x] == 0:
                        poslist.append([temp + 1, x])

                if board[y - 1][x - 1] != 0:
                    poslist.append([y - 1, x - 1])

                if board[y - 1][x + 1] != 0:
                    poslist.append([y - 1, x + 1])

                        
            if board[temp][x] == 0:
                poslist.append([temp, x])
           

        except:
            try:
                if board[temp][x] == 0:
                    poslist.append([temp, x])
                   
            except:
                pass

        return poslist



class Rook:

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


class Bishop:

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


class Knight():

    def validList(self, board, piece, y, x):
        poslist = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if abs(i - y) == 1 and abs(j - x) == 2:
                    if (board[i][j] * piece) <= 0:
                        poslist.append([i, j])

                elif abs(i - y) == 2 and abs(j - x) == 1:
                    if (board[i][j] * piece) <= 0:
                        poslist.append([i, j])

        return poslist


class King:

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
