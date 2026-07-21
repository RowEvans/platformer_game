import pygame

from platforms import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

RED = (255, 0, 0)

pygame.display.set_caption("Platformer")

active_sprites = pygame.sprite.Group()
player = Player()

level_list = [Level_01(player)]
current_level_idx = 0
current_level = level_list[current_level_idx]

player.level = current_level

active_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        player.handleEvent(event)
        if event.type == pygame.QUIT:
            running = False

    current_level.draw(screen)
    active_sprites.draw(screen)
    for sprite in active_sprites:
        pygame.draw.rect(screen, RED, sprite.rect, 1)
    
    player.update(screen)
    current_level.update()

    pygame.display.flip()
    pygame.key.set_repeat(50, 50)
    clock.tick(60)

pygame.quit()