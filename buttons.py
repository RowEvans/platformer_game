import pygame
import state
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button():
    def __init__(self, text, x, y, width, height, color, bg_color, id):
        
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color

        self.font = pygame.font.Font("platformer_game/assets/fonts/PixelOperator8.ttf", 48)
        self.text_surf = self.font.render(text, True, color, bg_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.id = id

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.id == 0:
                    state.game_over = False
                else:
                    pygame.quit()
                    sys.exit()