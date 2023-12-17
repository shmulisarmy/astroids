import pygame

#needed for font
pygame.init()

WIDTH, HEIGHT = 1450, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
scorefont = pygame.font.Font(None, 100)
qfont = pygame.font.Font(None, 35)
inputfont = pygame.font.Font(None, 50)
astroid = pygame.image.load('astroid.gif')
backround = pygame.transform.scale(pygame.image.load('space.png'), (WIDTH, HEIGHT))
star_image = pygame.transform.scale(pygame.image.load('star.png'), (7, 7))
play_button = pygame.transform.scale(pygame.image.load('play_button.png'), (100, 60))
life_diplay = pygame.transform.scale(pygame.image.load('live.png'), (100, 100))
starting_lives = 3
speed = HEIGHT//150