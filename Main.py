'''
This block imports the 2 modules I'll be using.
'''
import pygame, sys
from pygame.locals import *


'''
This block starts the game,
defines the dimesnions of the surface object
and creates the surface object 'screen'.
'''
pygame.init()
surfWidth = 1000
surfHeight = 600
screen = pygame.display.set_mode((surfWidth,surfHeight))


'''
This block defines a number of colours I'll be using,
by using denary RBG values stored in tuples for each one.
'''
white = (225,225,225)
black = (0,0,0)
red = (225,0,0)
green = (0,225,0)
blue = (0,0,225)
yellow = (225,225,0)
cyan = (0,225,225)
magenta = (225,0,225)


'''
This block calculates the coordinates of the centre pixel on the screen.
I need to do this because the positioning of many UI elements is centred
on the screen, or offset from the centre. It also fills the screen in white
because by default it's black, as well as define a list called grid that will
be used to store information about the cells in the grid on which the user
plays the game.
'''
xcentre = surfWidth/2
ycentre = surfHeight/2
screen.fill(white)
grid = []

fontObj = pygame.font.Font('freesansbold.ttf', 64)# Creates a font for all text.
fontObj2 = pygame.font.Font('freesansbold.ttf', 16)

checkText = fontObj2.render('Check answer', True, magenta, green)
checkTextRect = checkText.get_rect()
checkTextRect.center = (xcentre - 200, ycentre + 200)

backText = fontObj.render('Go back', True, cyan, black)
backTextRect = backText.get_rect()
backTextRect.center = (xcentre, ycentre + 200)

checked = fontObj.render('Your answer was checked', True, red, yellow)
checkedRect = checked.get_rect()
checkedRect.center = (xcentre, ycentre)

wrongText = fontObj.render('You\'re wrong you loser!', True, red, black)
wrongTextRect = wrongText.get_rect()
wrongTextRect.center = (xcentre, ycentre)

correctText = fontObj.render('Your answer was correct', True, green, white)
correctTextRect = correctText.get_rect()
correctTextRect.center = (xcentre, ycentre)

instructionsText = fontObj2.render('This is a simulation of Conway\'s game of life made into a puzzle game.', True, white, black)
instructionsTextRect = instructionsText.get_rect()
instructionsTextRect.center = (xcentre, (ycentre-(16*3)))

instructionsText2 = fontObj2.render('You are given a start condition as a grid and using 4 rules you must work', True, white, black)
instructionsTextRect2 = instructionsText2.get_rect()
instructionsTextRect2.center = (xcentre, (ycentre-(16*2)))

instructionsText3 = fontObj2.render('out what the condition will be in 1 moves time. These rules are:', True, white, black)
instructionsTextRect3 = instructionsText3.get_rect()
instructionsTextRect3.center = (xcentre, (ycentre-16))

instructionsText4 = fontObj2.render('any live cell with fewer than two live neighbours dies,', True, white, black)
instructionsTextRect4 = instructionsText4.get_rect()
instructionsTextRect4.center = (xcentre, ycentre)

instructionsText5 = fontObj2.render('any live cell with two or three live neighbours lives on to the next generation,', True, white, black)
instructionsTextRect5 = instructionsText5.get_rect()
instructionsTextRect5.center = (xcentre, (ycentre+16))

instructionsText6 = fontObj2.render('any live cell with more than three live neighbours dies,', True, white, black)
instructionsTextRect6 = instructionsText6.get_rect()
instructionsTextRect6.center = (xcentre, (ycentre+(16*2)))

instructionsText7 = fontObj2.render(' any dead cell with exactly three live neighbours becomes a live cell.', True, white, black)
instructionsTextRect7 = instructionsText7.get_rect()
instructionsTextRect7.center = (xcentre, (ycentre+(16*3)))

startText = fontObj.render('Start game', True, red, yellow)
startTextRect = startText.get_rect()
startTextRect.center = (xcentre, (ycentre+(16*8)))

howtoText = fontObj2.render('How to play', True, white, black)
howtoTextRect = howtoText.get_rect()
howtoTextRect.center = (xcentre + 200, ycentre + 200)

levelText = fontObj2.render('Level select', True, magenta, green)
levelTextRect = levelText.get_rect()
levelTextRect.center = (xcentre, ycentre + 200)

levelplaceholderText = fontObj2.render('This text is a placeholder for the level select screen!', True, magenta, green)
levelplaceholderTextRect = levelplaceholderText.get_rect()
levelplaceholderTextRect.center = (xcentre, ycentre)

howto2Text = fontObj.render('How to play', True, magenta, green)
howto2TextRect = howto2Text.get_rect()
howto2TextRect.center = (xcentre, ycentre + 200)

def drawGrid(gridWidth, gridHeight, moveGrid, saveInfo, xCord, yCord):
    counter = 0
    for i in range(1, gridWidth + 1):
        for n in range (1, gridHeight +1):
            if i % 10 == 0:
                if n % 10 ==0:
                    imod = (i /10)-1
                    x = i + imod + moveGrid
                    nmod = (n/10)-1
                    y = n+nmod
                    pygame.draw.rect(screen, red, (x, y, 10, 10))
                    if saveInfo == True:
                        grid.append([int(x), int(y), int(10), int(10), 'red', [xCord, yCord], int(0)])
                        if ( yCord % 35) == 0:
                            xCord += 1
                            yCord = 0
                        yCord += 1
                        counter += 1
                        #print(xCord, yCord)

def mainLoop():
    def instructionScreen():
        screen.fill(white)
        screen.blit(instructionsText, instructionsTextRect)
        screen.blit(instructionsText2, instructionsTextRect2)
        screen.blit(instructionsText3, instructionsTextRect3)
        screen.blit(instructionsText4, instructionsTextRect4)
        screen.blit(instructionsText5, instructionsTextRect5)
        screen.blit(instructionsText6, instructionsTextRect6)
        screen.blit(instructionsText7, instructionsTextRect7)
        screen.blit(startText, startTextRect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    pos = pygame.mouse.get_pos()
                    if startTextRect.collidepoint(pos):
                        gameScreen()
                        break
            pygame.display.update()
        
    def gameScreen():
        screen.fill(white)
        drawGrid(300, 350 ,0, False, 0, 0)
        drawGrid(300, 350 ,surfWidth - 349, True, 1, 1)
        screen.blit(checkText, checkTextRect)
        screen.blit(howtoText, howtoTextRect)
        screen.blit(levelText, levelTextRect)
        #global answer
        answer = grid
        answer[1049] [4] = 'green'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    pos = pygame.mouse.get_pos()
                    for cell in grid:
                        if mouseX in range(cell[0] - 1, cell[0] + cell[2]):
                            if mouseY in range(cell[1] - 1, cell[1] + cell[3]):
                                if cell[4] == 'red':
                                    cell[4] = 'green'
                                    pygame.draw.rect(screen, green, (cell[0], cell[1], cell[2], cell[3]))
                                else:
                                    cell[4] = 'red'
                                    pygame.draw.rect(screen, red, (cell[0], cell[1], cell[2], cell[3]))
                                print(grid.index(cell), answer[grid.index(cell)])
                    if checkTextRect.collidepoint(pos):
                        for cell in grid:
                            cell[6] = 0
                            x = cell[5][0]
                            y = cell[5][1]
                            if x == 1:         # if on left hand side
                                if y == 1: # if bottom left corner
                                    for cellNested in grid:
                                        if cellNested[5] == [2, 1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                        
                                        elif cellNested[5] == [2, 2] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                        
                                        elif cellNested[5] == [1, 2] and cellNested[4] == 'green':
                                            cell[6] += 1

                                elif y == 35: # if top left corner
                                    for cellNested in grid:
                                        if cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                            
                                        elif cellNested[5] == [x+1, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                            
                                        elif cellNested[5] == [x+1, y] and cellNested[4] == 'green':
                                            cell[6] += 1

                                else: # if on left hand side but not either left hand corner
                                    for cellNested in grid:
                                        if cellNested[5] == [x, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                            
                                        elif cellNested[5] == [x+1, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x+1, y] and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x+1, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1

                            elif y == 30: # if on right hand side
                                if cell[1] == 1: # if bottom right corner
                                    for cellNested in grid:
                                        elif cellNested[5] == [x-1, y+1] and cellN
                                        if cellNested[5] == [x-1, y]and cellNested[4] == 'green':
                                            cell[6] += 1
                                                    
                                        elif cellNested[5] == [x-1, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                    
                                        elif cellNested[5] == [x, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                elif y == 35: # if top right corner
                                    for cellNested in grid:
                                        if cellNested[5] == [x-1, y]and cellNested[4] == 'green':
                                            cell[6] += 1
                                                    
                                        elif cellNested[5] == [x-1, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                                    
                                        elif cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                else: # if on right hand side but not either right hand corner
                                    for cellNested in grid:
                                        if cellNested[5] == [x, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1
                                            
                                        elif cellNested[5] == [x-1, y+1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x-1, y]and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x-1, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1

                                        elif cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                            cell[6] += 1
                            
                            elif y == 1: # if bottom side but not either bottom corner
                                for cellNested in grid:
                                    if cellNested[5] == [x+1, y] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x+1, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y]and cellNested[4] == 'green':
                                        cell[6] += 1

                            elif y == 35: # if top side but not either top corner
                                for cellNested in grid:
                                    if cellNested[5] == [x+1, y] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x+1, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y] and cellNested[4] == 'green':
                                        cell[6] += 1
                            else: # if cell isn't on any of the 4 sides of the grid
                                for cellNested in grid:
                                    if cellNested[5] == [x+1, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1
                                            
                                    elif cellNested[5] == [x+1, y] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x+1, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y-1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x-1, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1

                                    elif cellNested[5] == [x, y+1] and cellNested[4] == 'green':
                                        cell[6] += 1
                        for cell in grid:
                            #pygame.display.update()
                            if cell[4] == 'green':
                                if (cell[6] < 2) or (cell[6] > 3) :
                                    pygame.draw.rect(screen, red, (cell[0], cell[1], 10, 10))
                                    #cell[4] = 'red'
                            else:
                                if cell[6] == 3:
                                    pygame.draw.rect(screen, green, (cell[0], cell[1], 10, 10))
                                    #cell[4] = 'green'
                        checkedScreen()
                        
                    elif howtoTextRect.collidepoint(pos):
                        instructionScreen()
                        break
                    elif levelTextRect.collidepoint(pos):
                        levelScreen()
                        break
            pygame.display.update()

    def checkedScreen():
        screen.fill(white)
        #screen.blit(checked, checkedRect)
        if answer == grid:
            screen.blit(correctText, correctTextRect)
            print('correct')
        else:
            screen.blit(wrongText, wrongTextRect)
            print ('wrong')
        
        screen.blit(backText, backTextRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if backTextRect.collidepoint(pos):
                        gameScreen()
            pygame.display.update()
         
    def levelScreen():
        screen.fill(white)
        screen.blit(startText, startTextRect)
        screen.blit(howto2Text, howto2TextRect)
        screen.blit(levelplaceholderText, levelplaceholderTextRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if howto2TextRect.collidepoint(pos):
                        instructionScreen()
                        break
                    elif startTextRect.collidepoint(pos):
                        gameScreen()
                        break
            pygame.display.update()
                        
    gameScreen()
while True:
    mainLoop()
