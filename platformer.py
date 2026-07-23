import pygame
import state

from levels import *
from player import *
from buttons import *

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

RED = (255, 0, 0)

pygame.display.set_caption("Platformer")

active_sprites = pygame.sprite.Group()
player = Player()

level_list = [Level_01(player), Level_02(player), Level_03(player)]
current_level_idx = 0
current_level = level_list[current_level_idx]

player.level = current_level

start_button = Button("START", 400, 300, 200, 100, WHITE, BLACK, 0, player)
quit_button = Button("QUIT", 700, 300, 200, 100, WHITE, BLACK, 1, player)

overlay = Transition()

active_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        player.handleEvent(event)
        start_button.handleEvent(event)
        quit_button.handleEvent(event)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    current_level.draw(screen)
    active_sprites.draw(screen)
    overlay.draw(screen)

    coin_collides = pygame.sprite.spritecollide(player, current_level.coin_list, False)
    if len(coin_collides) == 1:
        coin = coin_collides[0]
        coin.collect()
    
    for coin in current_level.coin_list:
        if coin.peaked and not overlay.active:
            overlay.start()
            break
        
    if state.game_over:
        pygame.event.set_blocked(pygame.KEYDOWN)
        start_button.draw(screen)
        quit_button.draw(screen)
    else:
        pygame.event.set_allowed(pygame.KEYDOWN)
    
    player.update()
    current_level.update()
    overlay.update()
    if overlay.peaked:
        overlay.peaked = False
        next_idx = current_level_idx + 1
        if next_idx < len(level_list):
            current_level_idx = next_idx
            current_level = level_list[current_level_idx]
            player.level = current_level
            player.reset()

    pygame.display.flip()
    pygame.key.set_repeat(50, 50)
    clock.tick(60)

pygame.quit()