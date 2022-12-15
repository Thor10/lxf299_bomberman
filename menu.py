import pygame
import game
from algorithm import Algorithm

COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.NONE
en3_alg = Algorithm.NONE
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 800
Y = 800
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font('freesansbold.ttf', 42)
 
# Start Game Menu Option

# create a text surface object,
# on which text is drawn on it.
startGameText = font.render('START GAME', True, green, blue)

# create a rectangular object for the
# text surface object
startGameTextRect = startGameText.get_rect()
 
# set the center of the rectangular object.
startGameTextRect.center = (X // 2, (Y // 2) - 200)

# Options menu option

optionGameText = font.render('OPTIONS', True, green, blue)
optionGameTextRect = optionGameText.get_rect()
optionGameTextRect.center = (X // 2, (Y // 2))

# Exit menu option

exitGameText = font.render('EXIT', True, green, blue)
exitGameTextRect = exitGameText.get_rect()
exitGameTextRect.center = (X // 2, (Y //2) + 200)

def optionsMenuProcess():
    # Options menu processing
    global en1_alg
    global en2_alg
    global en3_alg
    
    optionsMenuEnd = False
    
    playerTwoValue = 'PLAYER TWO: DIJKSTRA'
    playerThreeValue = 'PLAYER THREE: NONE'
    playerFourValue = 'PLAYER FOUR: NONE'
    
    # Set Player Two Text
    playerTwoText = font.render(playerTwoValue, True, green, blue)
    playerTwoTextRect = playerTwoText.get_rect()
    playerTwoTextRect.center = (X // 2, (Y // 2) - 200)
    
    # Set Player Three Text
    playerThreeText = font.render(playerThreeValue, True, green, blue)
    playerThreeTextRect = playerThreeText.get_rect()
    playerThreeTextRect.center = (X // 2, (Y // 2) - 100)
    
    # Set Player Four Text
    playerFourText = font.render(playerFourValue, True, green, blue)
    playerFourTextRect = playerFourText.get_rect()
    playerFourTextRect.center = (X // 2, (Y // 2))
    
    # Back button text
    backText = font.render('BACK', True, green, blue)
    backTextRect = backText.get_rect()
    backTextRect.center = (X // 2, (Y // 2) + 100)
    
    while optionsMenuEnd == False:
        # completely fill the surface object
        # with white color
        display_surface.fill(blue)
 
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(playerTwoText, playerTwoTextRect)
        display_surface.blit(playerThreeText, playerThreeTextRect)
        display_surface.blit(playerFourText, playerFourTextRect)
        display_surface.blit(backText, backTextRect)
 
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
 
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
 
                # deactivates the pygame library
                pygame.quit()
 
                # quit the program.
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # print('Left Mouse button pressed')
                pos = pygame.mouse.get_pos()
                
                if pos[0] >= playerTwoTextRect.topleft[0] and pos[0] <= playerTwoTextRect.topright[0] and pos[1] <= playerTwoTextRect.bottomright[1] and pos[1] >= playerTwoTextRect.topleft[1]:
                    #game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)
                    #display_surface = pygame.display.set_mode((X, Y))
                    if en1_alg == Algorithm.DIJKSTRA:
                        playerTwoValue = 'PLAYER TWO: DFS'
                        en1_alg = Algorithm.DFS
                    elif en1_alg == Algorithm.DFS:
                        playerTwoValue = 'PLAYER TWO: NONE'
                        en1_alg = Algorithm.NONE
                    elif en1_alg == Algorithm.NONE:
                        playerTwoValue = 'PLAYER TWO: DIJKSTRA'
                        en1_alg = Algorithm.DIJKSTRA
                        
                    playerTwoText = font.render(playerTwoValue, True, green, blue)
                
                if pos[0] >= playerThreeTextRect.topleft[0] and pos[0] <= playerThreeTextRect.topright[0] and pos[1] <= playerThreeTextRect.bottomright[1] and pos[1] >= playerThreeTextRect.topleft[1]:
                    # print('OPTION PRESSED')
                    if en2_alg == Algorithm.DIJKSTRA:
                        playerThreeValue = 'PLAYER THREE: DFS'
                        en2_alg = Algorithm.DFS
                    elif en2_alg == Algorithm.DFS:
                        playerThreeValue = 'PLAYER THREE: NONE'
                        en2_alg = Algorithm.NONE
                    elif en2_alg == Algorithm.NONE:
                        playerThreeValue = 'PLAYER THREE: DIJKSTRA'
                        en2_alg = Algorithm.DIJKSTRA
                        
                    playerThreeText = font.render(playerThreeValue, True, green, blue)
                    
                if pos[0] >= playerFourTextRect.topleft[0] and pos[0] <= playerFourTextRect.topright[0] and pos[1] <= playerFourTextRect.bottomright[1] and pos[1] >= playerFourTextRect.topleft[1]:
                    # print('OPTION PRESSED')
                    if en3_alg == Algorithm.DIJKSTRA:
                        playerFourValue = 'PLAYER FOUR: DFS'
                        en3_alg = Algorithm.DFS
                    elif en3_alg == Algorithm.DFS:
                        playerFourValue = 'PLAYER FOUR: NONE'
                        en3_alg = Algorithm.NONE
                    elif en3_alg == Algorithm.NONE:
                        playerFourValue = 'PLAYER FOUR: DIJKSTRA'
                        en3_alg = Algorithm.DIJKSTRA
                        
                    playerFourText = font.render(playerFourValue, True, green, blue)
                
                if pos[0] >= backTextRect.topleft[0] and pos[0] <= backTextRect.topright[0] and pos[1] <= backTextRect.bottomright[1] and pos[1] >= backTextRect.topleft[1]:
                    optionsMenuEnd = True
 
            # Draws the surface object to the screen.
            pygame.display.update()



mainMenuEnd = False 
# infinite loop
while mainMenuEnd == False:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(blue)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(startGameText, startGameTextRect)
    display_surface.blit(optionGameText, optionGameTextRect)
    display_surface.blit(exitGameText, exitGameTextRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # print('Left Mouse button pressed')
            pos = pygame.mouse.get_pos()
            if pos[0] >= startGameTextRect.topleft[0] and pos[0] <= startGameTextRect.topright[0] and pos[1] <= startGameTextRect.bottomright[1] and pos[1] >= startGameTextRect.topleft[1]:
                game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)
                display_surface = pygame.display.set_mode((X, Y))
                
            if pos[0] >= optionGameTextRect.topleft[0] and pos[0] <= optionGameTextRect.topright[0] and pos[1] <= optionGameTextRect.bottomright[1] and pos[1] >= optionGameTextRect.topleft[1]:
                optionsMenuProcess()

            if pos[0] >= exitGameTextRect.topleft[0] and pos[0] <= exitGameTextRect.topright[0] and pos[1] <= exitGameTextRect.bottomright[1] and pos[1] >= exitGameTextRect.topleft[1]:
                mainMenuEnd = True
 
        # Draws the surface object to the screen.
        pygame.display.update()
pygame.quit()


# game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)
