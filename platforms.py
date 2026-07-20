import pygame

#globals
sky_blue = (173, 216, 230)
tan = (214, 181, 136)
black = (0, 0, 0)


class Platform(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Level(object):
    #Parent class
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.background = None

    def update(self):
        #update everything
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        #draw everything

        screen.fill(sky_blue)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        #platforms (width, height, x, y)
        level = [[100, 200, 100, 500],
                 [100, 200, 300, 400],
                 [100, 200, 600, 500]]
        
        for platform in level:
            block = Platform(tan, platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
