import random
import settings
import pygame

class Question:
    speed = settings.HEIGHT//150
    question_upto = 0
    
    def __init__(self):
        self.q_index = Question.question_upto%len(a_s)
        self.q = qs[self.q_index]
        self.a = a_s[self.q_index]
        self.q_render = settings.qfont.render(self.q, True, (200, 0, 255))  # Render text with white color
        self.width = len(self.q) * 13
        self.height = 35
        self.x = random.randint(0, settings.WIDTH - self.width)
        self.y = 0
        self.p_g_o = pygame.Rect(self.x, self.y, self.width, self.height)
        self.astroid = pygame.transform.scale(settings.astroid, (self.width*2, self.height*3))
        Question.question_upto += 1
        Question.speed *= 1.03

    def display(self):
        settings.window.blit(self.astroid, (self.x-70, self.y-40))
        # pygame.draw.rect(settings.window, (255, 255, 255), self.p_g_o)
        settings.window.blit(self.q_render, (self.x, self.y, self.width, self.height))

    def move_down(self):
        self.y += Question.speed
        self.p_g_o[1] = self.y


a_s = [
    "cat", "dog", "hat", "run", "cup", "bat", "sat", "tap", "map", "bag",
    "log", "pen", "fox", "joy", "jump", "quick", "lazy", "brown", "zebra",
    "elephant", "excellent", "complicated", "encyclopedia", "parallelogram",
    "xylophone", 'how', 'how'
]

a_s.sort(key = lambda word: len(word))


qs = [
    f'type in {i}' for i in a_s
]