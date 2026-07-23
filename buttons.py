import pygame
import state
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button():
    def __init__(self, text, x, y, color, bg_color, id, player):
        
        self.bg_color = bg_color

        self.font = pygame.font.Font("platformer_game/assets/fonts/PixelOperator8.ttf", 48)
        self.text_surf = self.font.render(text, True, color, bg_color)
        self.text_rect = self.text_surf.get_rect(topleft=(x, y))
        self.id = id
        self.player = player

    def draw(self, screen):
        new_rect = pygame.Rect(self.text_rect.x - 5, self.text_rect.y - 5, self.text_rect.width + 10, self.text_rect.height + 10)
        pygame.draw.rect(screen, self.bg_color, new_rect, border_radius=5)
        screen.blit(self.text_surf, self.text_rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.text_rect.collidepoint(event.pos):
                if self.id == 0:
                    state.game_over = False
                    self.player.reset()
                else:
                    pygame.quit()
                    sys.exit()