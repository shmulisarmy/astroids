import random
import settings
import pygame
import main
import sys

class page():
    def __init__(self) -> None:
        self.stars_list = [(random.randint(0, settings.WIDTH), random.randint(0, settings.HEIGHT)) for _ in range(40)]

    def draw_stars(self):
        for star_location in self.stars_list:
            settings.window.blit(settings.star_image, star_location)

    def draw_button(self):
        settings.window.blit(settings.play_button, (settings.WIDTH/2 - 50, settings.HEIGHT/2 - 30))

    def draw_all(self):
        settings.window.fill('black')
        self.draw_stars()
        self.draw_button()
        pygame.display.update()

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.mouse.get_pressed()[1] or pygame.key.get_pressed()[pygame.K_UP]:
                    print('mouse down')
                    mx, my = pygame.mouse.get_pos()
                    mouse_on_play_button = (
                        settings.WIDTH//2 - 50 < mx < settings.WIDTH//2 + 50 
                        and settings.HEIGHT//2 - 30 < my < settings.HEIGHT//2 + 30)
                    if mouse_on_play_button:
                        game = main.Game()
                        game.run_game()

            self.draw_all()

page().run()

    