import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#Level Editor Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

#Set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))

pygame.display.set_caption("Level Editor")

#Define Game Variables
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

#Define Colors
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

#Load Images
pine1_img = pygame.image.load('Images/Background-Images/pine1.png').convert_alpha()
pine2_img = pygame.image.load('Images/Background-Images/pine2.png').convert_alpha()
mountain_img = pygame.image.load('Images/Background-Images/mountain2.png').convert_alpha()
sky_img = pygame.image.load('Images/Background-Images/sky_cloud.png').convert_alpha()

def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
    for x in range(4):
        screen.blit(sky_img, ((x * width) - scroll * 0.5 ,0))
        screen.blit(mountain_img, ((x * width) - scroll * 0.6, mountain_img.get_height()))
        screen.blit(pine1_img, ((x * width) - scroll * 0.7 , pine1_img.get_height()))
        screen.blit(pine2_img, ((x * width) - scroll * 0.8, pine2_img.get_height()))

#Draw Grid
def draw_grid():
    #Vertical Lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))

    #Horizontal Lines
    for r in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE))


#Running Level Editor
running = True

while running:

    clock.tick(FPS)

    draw_bg()
    draw_grid()

    #Scroll Map
    if scroll_left == True and scroll > 0:
        scroll -= (2.5 * scroll_speed)
    if scroll_right == True and scroll < 1000:
        scroll += (2.5 * scroll_speed)


    #Key Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True

            if event.key == pygame.K_RIGHT:
                scroll_right = True

            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False

            if event.key == pygame.K_RIGHT:
                scroll_right = False 

            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()

pygame.QUIT()