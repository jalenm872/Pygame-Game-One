import pygame

#Create a player class
class Player:
    def __init__(self):
        self.playerX = 370
        self.playerY = 480
        self.playerHealth = 100
        self.playerGravity = 0
        self.playerX_change = 0
        self.playerY_change = 0

    # Handle player movement
    def move(self):
        self.playerX += self.playerX_change
        self.playerY += self.playerY_change

    # Handle player controls
    def handleControls(self, event):
        # If keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 0.3
            if event.key == pygame.K_UP:
                self.playerY_change -= 0.3

        # If keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0
            if event.key == pygame.K_UP:
                self.playerY_change = 0

    def handleBoundaries(self):
        # Player boundaries
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1000:
            self.playerX = 1000
        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 700:
            self.playerY = 700

    def update(self, event):
        self.handleControls(event)
        self.move()
        self.handleBoundaries()

