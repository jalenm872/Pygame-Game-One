import pygame
from player import Player

# Initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 640))
print("Hello")

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

# While the game is running
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((91,153,139))

    #Update the player
    player.update(event)
        
    # Draw the player
    screen.blit(playerImg, (player.playerX, player.playerY))

    # Update the screen
    pygame.display.update()