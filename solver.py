import pygame

# Globals
size = width, height = 458, 458
rows = cols = 9
tileSize = width//rows

white = (255,255,255)
black = (0,0,0)
grey = (220,220,220)

#Function 
def backtrack(board, screen, animate):
    solved = False
    for row in range(9):
        for col in range(9):
            if board[row][col][1] == 0:
                for value in range(1,10):
                    board[row][col][1] = value
                    if(animate):
                        draw_board(screen,board)
                    validMove = validate(board,row,col)
                    if validMove:
                        solved = backtrack(board,screen,animate)
                        if solved:
                            return True
                board[row][col][1] = 0
                return
    return True

def validate(board,currRow,currCol):
    #validate row
    counter = 0
    for value in board[currRow]:
        if board[currRow][currCol][1] == value[1]:
            counter += 1
    if counter > 1:
        return False

    #validate col
    counter = 0
    for row in board:
        if board[currRow][currCol][1] == row[currCol][1]:
            counter += 1
    if counter > 1:
        return False
    
    #validate grid
    gridRow = int(currRow/3) * 3
    gridCol = int(currCol/3) * 3
    counter = 0
    for row in range(gridRow, gridRow+3):
        for col in range(gridCol, gridCol+3):
            if board[currRow][currCol][1] == board[row][col][1]:
                counter += 1
    if counter > 1:
        return False

    return True


def initial_board(boardFile):
    with open(boardFile, "r") as gameFile:
        board = []
        for line in gameFile:
            row = []
            for value in line:
                editable = False
                if value != '\n':
                    if value == '0':
                        editable = True
                    entry = [editable,int(value)]
                    row.append(entry)
            board.append(row)
    return board

def draw_board(screen, board):
    offset = 4
    digitFont = pygame.font.SysFont(None, 50)

    #Draw White Background (workaround for blinking buttons)
    background = pygame.Rect(offset,offset,width,height)
    pygame.draw.rect(screen,white,background)

    #Draw Tiles
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(tileSize*col+offset, tileSize*row+offset, tileSize, tileSize)
            pygame.draw.rect(screen,grey,rect, 1)

    #Draw Grid
    for row in range (rows//3):
        row *=3
        for col in range(cols//3):
            col*=3
            rect = pygame.Rect(tileSize*col+offset, tileSize*row+offset, 3*tileSize, 3*tileSize)
            pygame.draw.rect(screen,black,rect,1)

    #Draw Numbers
    currRow = currCol = 0
    for row in board:
        for value in row:
            if(value[1] != 0):
                digit = digitFont.render(str(value[1]),black,True)
                xPos = currCol*tileSize + tileSize//2 + offset - digit.get_rect().width//2
                yPos = currRow*tileSize + tileSize//2 +  offset - digit.get_rect().height//2
                screen.blit(digit, (xPos,yPos))
            currCol += 1
        currRow += 1
        currCol = 0
    
    pygame.display.flip()