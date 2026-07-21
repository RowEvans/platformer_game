import pygame

#globals
SKY_BLUE = (173, 216, 230)
TAN = (214, 181, 136)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        spritesheet = pygame.image.load("platformer_game/assets/sprites/platforms.png")
        sprite_rect = pygame.Rect(16, 0, 32, 9)
        frame = spritesheet.subsurface(sprite_rect)

        size = (200, 100)
        self.image = frame
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        spritesheet = pygame.image.load("platformer_game/assets/sprites/spike.png")
        sprite_rect = pygame.Rect(0,0, 16, 16)

        spike = spritesheet.subsurface(sprite_rect)

        size = (40, 40)
        self.image = spike
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

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

        screen.fill(SKY_BLUE)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

        for sprite in self.platform_list:
            pygame.draw.rect(screen, RED, sprite.rect, 1)

class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        #platforms (width, height, x, y)
        level = [(100, 500),
                 (300, 400),
                 (600, 500),
                 (900, 500),
                 (1080, 400)]
        
        for platform in level:
            block = Platform(platform)
            block.player = self.player
            self.platform_list.add(block)

        enemies = [(700, 460)]

        for enemy in enemies:
            spike = Enemy(enemy)
            spike.player = self.player
            self.enemy_list.add(spike)
