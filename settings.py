import pygame

#needed for font
pygame.init()

WIDTH, HEIGHT = 1450, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
scorefont = pygame.font.Font(None, 100)
qfont = pygame.font.Font(None, 35)
inputfont = pygame.font.Font(None, 50)
backround = pygame.transform.scale(pygame.image.load('space.png'), (WIDTH, HEIGHT))
life_diplay = pygame.transform.scale(pygame.image.load('live.png'), (100, 100))
# display_input = pygame.Rect(0, )