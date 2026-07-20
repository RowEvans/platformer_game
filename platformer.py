import pygame

from platforms import *
from player import Player

pygame.init()
sky_blue = (173, 216, 230)
tan = (214, 181, 136)
black = (0, 0, 0)

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

gravity = 1
friction = 1

sprite_group = pygame.sprite.Group()
player = Player(black, 50, 50, 200, 100, 0, 0)
level = Level_01(player)

sprite_group.add(player)

running = True

while running:
    for event in pygame.event.get():
        player.handleEvent(event)
        if event.type == pygame.QUIT:
            running = False

    #if player.isCollidePlatform(platform):
    #    player.y_velo += gravity        
    #else: 
    #    player.rect.y = platform.rect.y - player.rect.height
    #    player.y_velo = 0
    
    if player.x_velo > 0:
        player.x_velo -= friction
    elif player.x_velo < 0:
        player.x_velo += friction

    screen.fill(sky_blue)
    sprite_group.draw(screen)
    level.draw(screen)
    
    player.update()
    level.update()

    pygame.display.flip()
    pygame.key.set_repeat(50, 50)
    clock.tick(60)

pygame.quit()