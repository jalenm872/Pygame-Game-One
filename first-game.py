import pygame
from player import Player

# Initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((1000, 800))

# Title and Icon
# Caption is the title of the window
pygame.display.set_caption("Jeraldyn")
# Icon is the image on the top left of the window
#icon = pygame.image.load('ufo.png')
# Set the icon
#pygame.display.set_icon(icon)

# Player Images
playerImg = pygame.image.load('Images/Main-Character/character-0.png')

# Create Instance of player
player = Player()

# Game loop
running = True


def playerControls():

    # Player coordinates
    playerX = 370
    playerY = 480

    # Player movement
    playerX_change = 0
    playerY_change = 0

    # If keystroke is pressed, check whether it's right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
        if event.key == pygame.K_UP:
            playerY_change -= 0.3
        if event.key == pygame.K_DOWN:
            playerY_change += 0.3

    # If keystroke is released, check whether it's right or left
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    # Update player position
    playerX += playerX_change
    playerY += playerY_change


    # Boundaries for the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1000:
        playerX = 1000

    if playerY <= 0:
        playerY = 0
    elif playerY >= 800:
        playerY = 800


while running:

    # RGB - Red, Green, Blue
    screen.fill((91,153,139))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerControls()

    #     # If keystroke is pressed, check whether it's right or left
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             playerX_change = -0.3
    #         if event.key == pygame.K_RIGHT:
    #             playerX_change = 0.3
    #         if event.key == pygame.K_UP:
    #             playerY_change -= 0.3
    #         if event.key == pygame.K_DOWN:
    #             playerY_change += 0.3

    #     # If keystroke is released, check whether it's right or left
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #             playerX_change = 0
    #         if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #             playerY_change = 0

    # # Update player position
    # playerX += playerX_change
    # playerY += playerY_change


    # # Boundaries for the player
    # if playerX <= 0:
    #     playerX = 0
    # elif playerX >= 1000:
    #     playerX = 1000

    # if playerY <= 0:
    #     playerY = 0
    # elif playerY >= 800:
    #     playerY = 800

    # Draw the player
    screen.blit(playerImg, (playerX, playerY))

    # Update the screen
    pygame.display.update()
