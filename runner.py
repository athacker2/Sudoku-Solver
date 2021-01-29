import pygame
import solver as sudoku

from pygame.locals import (
    K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_s
)

pygame.init()

white = (255,255,255)
black = (0,0,0)
dark_grey = (100,100,100)
buttonFont = pygame.font.SysFont(None, 21)

board_size = board_width, board_height = 458, 458
rows = cols = 9
tileSize = board_width//rows
board_offset = 4

screen_size = screen_width, screen_height = 458, 508
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sudoku")

running = True

active_board = "board2.txt"
board = sudoku.initial_board(active_board)


while running:
    mousePressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True


    screen.fill(white)

    #Draw Buttons
    clear_button = pygame.Rect(int(tileSize*1.5-tileSize) + board_offset, rows*tileSize + (screen_height-board_height)//2, tileSize*2, tileSize//2)
    pygame.draw.rect(screen,dark_grey,clear_button)
    
    clear_text = buttonFont.render("Clear Board",black,True)
    xPos = int(tileSize*1.5-tileSize) + board_offset + tileSize - clear_text.get_rect().width/2
    yPos = rows*tileSize + (screen_height-board_height)//2 + tileSize//4 - clear_text.get_rect().height/2
    screen.blit(clear_text, (xPos,yPos))


    solve_button = pygame.Rect(int(tileSize*4.5-tileSize), rows*tileSize + (screen_height-board_height)//2, tileSize*2, tileSize//2)
    pygame.draw.rect(screen,dark_grey,solve_button)

    solve_text = buttonFont.render("Solve Board",black,True)
    xPos = int(tileSize*4.5-tileSize) + board_offset + tileSize - solve_text.get_rect().width/2
    yPos = rows*tileSize + (screen_height-board_height)//2 + tileSize//4 - solve_text.get_rect().height/2
    screen.blit(solve_text, (xPos,yPos))

    solve_quick_button = pygame.Rect(int(tileSize*7.5-tileSize), rows*tileSize + (screen_height-board_height)//2, tileSize*2, tileSize//2)
    pygame.draw.rect(screen,dark_grey,solve_quick_button)

    solve_quick_text = buttonFont.render("Solve Quick",black,True)
    xPos = int(tileSize*7.5-tileSize) + board_offset + tileSize - solve_quick_text.get_rect().width/2
    yPos = rows*tileSize + (screen_height-board_height)//2 + tileSize//4 - clear_text.get_rect().height/2
    screen.blit(solve_quick_text, (xPos,yPos))

    #Draw Board
    sudoku.draw_board(screen,board)

    

    #Check for User Input
    keys_pressed = pygame.key.get_pressed()
    solve = False
    animate = False

    if mousePressed:
        if(clear_button.collidepoint(pygame.mouse.get_pos())):
            board = sudoku.initial_board(active_board)
        elif(solve_button.collidepoint(pygame.mouse.get_pos())):
            solve = True
            animate = True
        elif(solve_quick_button.collidepoint(pygame.mouse.get_pos())):
            solve = True

    if(keys_pressed[K_0]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 0
    elif(keys_pressed[K_1]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 1
    elif(keys_pressed[K_2]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 2
    elif(keys_pressed[K_3]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 3
    elif(keys_pressed[K_4]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 4
    elif(keys_pressed[K_5]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 5
    elif(keys_pressed[K_6]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 6
    elif(keys_pressed[K_7]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 7
    elif(keys_pressed[K_8]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 8
    elif(keys_pressed[K_9]):
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid = (int(mouse_pos[1]/tileSize),int(mouse_pos[0]/tileSize))
        if(board[mouse_grid[0]][mouse_grid[1]][0]):
            board[mouse_grid[0]][mouse_grid[1]][1] = 9
    
    if solve:
        solve = False
        board = sudoku.initial_board(active_board)
        print("Solving")
        sudoku.backtrack(board, screen, animate)
        print("Finished")

    pygame.display.flip()

pygame.quit()
            