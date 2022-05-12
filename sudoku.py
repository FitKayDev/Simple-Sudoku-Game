#import and initialize the pygame library
#from turtle import position
import pygame

pygame.font.init()

WIDTH = 600
background_color = ('white')
grid_color = ('black')
screen = pygame.display.set_mode((WIDTH, WIDTH))
#for when we superimpose on grid and entire line gets edited
edits = 5

font1 = pygame.font.SysFont('Comic Sans MS', 35)

#Default Sudoku Board

grid = [
    [0, 0, 0, 1, 2, 0, 0, 0, 0],
    [1, 6, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 8, 7, 4, 6, 0, 0, 9],
    [9, 1, 0, 0, 7, 2, 0, 6, 0],
    [0, 0, 7, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 6, 3, 8, 1, 9, 7],
    [0, 0, 0, 2, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 4, 0, 0, 1, 0, 9, 0, 0]
    ]

player_grid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def play(screen, position):
    i, j = position[1], position[0]
    
    font1 = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #player tries to edit grid
                if (player_grid[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with zero
                    grid[i-1][j-1] == event.key - 48   

                    # player edits their input by making screen blank
                    #superimpose another block of same color above that block 
                    pygame.draw.rect(screen, background_color, (position[0]*50 + edits, position[1]*50 + edits, 50 - 2*edits, 50 - 2*edits))
                    pygame.display.update()
                # checking if inputs are valid 
                if(0 < event.key - 48 < 10):  
                    pygame.draw.rect(screen, background_color, (position[0]*50 + edits, position[1]*50 + edits, 50 - 2*edits, 50 - 2*edits))
                    value = font1.render(str(event.key-48), True, ('purple'))
                    screen.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    
                    return
                return    


def main():
    pygame.init()
    #window
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    #Set the title 
    pygame.display.set_caption("SUDOKU GAME")
    screen.fill(background_color)
    font1 = pygame.font.SysFont('Comic Sans MS', 35)

    #drawing the grid lines

    for i in range(0, 10):  
        #every third line must be bold to create a separate square within the game
        if(i%3 == 0) :
            pygame.draw.line(screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
            
        pygame.draw.line(screen, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
    
        
    pygame.display.update()   

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            #To only display the actual numbers and not the zeros
            if grid[i][j] != 0:
                value = font1.render(str(grid[i][j]), True, grid_color)
                screen.blit(value,( (j+1)*50 + 15, (i+1)*50))
    pygame.display.update()        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                play(screen, (pos[0]//50,pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()   