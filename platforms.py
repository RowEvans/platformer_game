import pygame

class Platform():
    def __init__(self, color, height, width, x, y):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)