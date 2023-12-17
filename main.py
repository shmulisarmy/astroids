import pygame
import settings
import questions
import sys
import random

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = 20
        self.bgcolor = 'black'
        self.pixel_x = 0
        self.pixel_y = 0
        self.score = 0
        self.input = ""
        self.score_render = settings.scorefont.render(f'score : {self.score}', True, (255, 255, 255))
        self.input_render = settings.inputfont.render(self.input, True, (255, 200, 200))
        self.display_change_score = 0
        self.lives = settings.starting_lives
        self.time_left = 120
        pygame.init()

    def display(self):
        settings.window.fill(self.bgcolor)
        settings.window.blit(settings.backround, (0, 0))
        self.cur_question.display()
        settings.window.blit(self.score_render, (0, 0))
        settings.window.blit(self.input_render, (settings.WIDTH//2 - 20, settings.HEIGHT - 50))
        for i in range(self.lives):
            settings.window.blit(settings.life_diplay, (settings.WIDTH - settings.starting_lives*100 + i*100, 0))
        if self.display_change_score:
                self.display_change_score -= 1
                dcsc = self.display_change_score
                settings.window.blit(settings.scorefont.render(str(self.recently_changed_num) if self.recently_changed_num < 0 else f'+{self.recently_changed_num}', True, (dcsc*4, dcsc*4, dcsc*4)), self.display_change_score_pos)
        pygame.display.update()

    def draw_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                pygame.draw.rect(self.window, (0,0,0), pygame.Rect(self.pixel_x * j, self.pixel_y * i, self.pixel_x, self.pixel_y))

    def controls(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w]:
            pass

    def change_score(self, num):
        self.recently_changed_num = num
        self.score += num
        self.score_render = settings.scorefont.render(f'score: {self.score}', True, (255, 255, 255))
        self.display_change_score_pos = (random.randint(settings.WIDTH-400, settings.WIDTH-200), random.randint(100, 300))
        self.display_change_score = 60
    def run_game(self):
        running = True
        self.cur_question = questions.Question()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.input == self.cur_question.a:
                            self.change_score(int(((settings.HEIGHT - self.cur_question.y)*(len(self.cur_question.q))*settings.speed)/1_000))
                            self.cur_question = questions.Question()
                        self.input = ""  
                    elif event.key == pygame.K_BACKSPACE:
                        self.input = self.input[:-1] 
                    else:
                        self.input += event.unicode  
                    self.input_render = settings.inputfont.render(self.input, True, (255, 200, 200))

            self.clock.tick(self.FPS)

            self.cur_question.move_down()
            if self.cur_question.y > settings.HEIGHT:
                self.cur_question = questions.Question()
                self.lives -= 1

            self.display()

if __name__ == '__main__':
    game = Game()
    game.run_game()