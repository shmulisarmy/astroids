import pygame, sys

#needed for font
pygame.init()

WIDTH, HEIGHT = 1450, 800
#needs to be before class is defined
if len(sys.argv) > 2:
    WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])

window = pygame.display.set_mode((WIDTH, HEIGHT))
scorefont = pygame.font.Font(None, WIDTH//14)
qfont = pygame.font.Font(None, WIDTH//40)
inputfont = pygame.font.Font(None, WIDTH//28)
astroid_size = HEIGHT//14
astroid = pygame.image.load('astroid.gif')
backround = pygame.transform.scale(pygame.image.load('space.png'), (WIDTH, HEIGHT))
star_image = pygame.transform.scale(pygame.image.load('star.png'), (7, 7))
play_button = pygame.transform.scale(pygame.image.load('play_button.png'), (WIDTH//14, HEIGHT//8))
life_diplay = pygame.transform.scale(pygame.image.load('live.png'), (WIDTH//14, HEIGHT//8))
starting_lives = 3
speed = HEIGHT//150