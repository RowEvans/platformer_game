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

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        spritesheet = pygame.image.load("platformer_game/assets/sprites/coin.png")

        frame_width = 16
        frame_height = 16

        self.coin_frames = []
        coin_frames_num = 12
        for i in range(coin_frames_num):
            x = i * 16
            sprite_rect = pygame.Rect(x, 0, frame_width, frame_height)

            frame = spritesheet.subsurface(sprite_rect)
            self.coin_frames.append(frame)

        coin = spritesheet.subsurface(sprite_rect)

        self.size = (40, 40)
        self.image = coin
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x, self.rect.y = pos
        self.y_velo = 0
        self.collected = False
        self.peaked = False

        self.frame_counter = 0
        self.frame_idx = 0

    def update(self):
        pygame.sprite.Sprite.update(self)

        if self.collected:
            self.rect.y += self.y_velo
            self.updCollected()

        self.frame_counter += 1

        if self.frame_counter >= 5:
            self.frame_counter = 0

            self.frame_idx = (self.frame_idx + 1) % len(self.coin_frames)

            self.image = self.coin_frames[self.frame_idx]
            self.image = pygame.transform.scale(self.image, self.size)
    
    def collect(self):
        if not self.collected:
            self.collected = True
            self.y_velo = -12
            self.peaked = False

    def updCollected(self):
        resistance = 1

        if self.y_velo < 0:
            self.y_velo += resistance
            if self.y_velo >= 0:
                self.peaked = True

class Transition():
    def __init__(self):
        self.overlay = pygame.Surface((1280, 720))
        self.overlay.fill(BLACK)
        self.alpha = 0
        self.fading_in = True
        self.active = False
        self.peaked = False
        self.overlay.set_alpha(0)

    def start(self):
        self.active = True
        self.fading_in = True
        self.alpha = 0

    def draw(self, screen):
        if self.active:
            screen.blit(self.overlay, (0, 0))
    def update(self):
        if not self.active:
            return

        step = 10

        if self.fading_in:
            self.alpha += step
            if self.alpha >= 255:
                self.alpha = 255
                self.fading_in = False
                self.peaked = True
        else:
            self.alpha -= step
            if self.alpha <= 0:
                self.alpha = 0
                self.active = False

        self.overlay.set_alpha(self.alpha) 

class Level(object):
    #Parent class
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.player = player

        self.background = None

    def update(self):
        #update everything
        self.platform_list.update()
        self.enemy_list.update()
        self.coin_list.update()

    def draw(self, screen):
        #draw everything

        screen.fill(SKY_BLUE)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.coin_list.draw(screen)

class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        #platforms (width, height, x, y)
        level = [(0, 500),
                 (100, 500),
                 (200, 500),
                 (300, 500),
                 (400, 500),
                 (500, 500),
                 (600, 500),
                 (700, 500),
                 (800, 500),
                 (900, 500),
                 (1000, 500),
                 (1100, 500),
                 (1200, 500)]
        
        for platform in level:
            block = Platform(platform)
            block.player = self.player
            self.platform_list.add(block)

        enemies = [(600, 460)]

        for enemy in enemies:
            spike = Enemy(enemy)
            spike.player = self.player
            self.enemy_list.add(spike)

        coins = [(1180, 450)]

        for coin in coins:
            coin_sprite = Coin(coin)
            coin_sprite.player = self.player
            self.coin_list.add(coin_sprite)

class Level_02(Level):
    def __init__(self, player):
        super().__init__(player)

        #platforms (width, height, x, y)
        level = [(100, 500),
                 (300, 500),
                 (500, 500),
                 (680, 400),
                 (880, 400),
                 (1080, 300)]
        
        for platform in level:
            block = Platform(platform)
            block.player = self.player
            self.platform_list.add(block)

        enemies = [(350, 460),
                   (700, 360)]

        for enemy in enemies:
            spike = Enemy(enemy)
            spike.player = self.player
            self.enemy_list.add(spike)

        coins = [(1180, 250)]

        for coin in coins:
            coin_sprite = Coin(coin)
            coin_sprite.player = self.player
            self.coin_list.add(coin_sprite)

class Level_03(Level):
    def __init__(self, player):
        super().__init__(player)

        #platforms (width, height, x, y)
        level = [(100, 620),
                 (450, 550), 
                 (800, 500),
                 (1000, 400),
                 (700, 250),
                 (400, 200)]

        for platform in level:
            block = Platform(platform)
            block.player = self.player
            self.platform_list.add(block)

        coins = [(500, 150)]

        for coin in coins:
            coin_sprite = Coin(coin)
            coin_sprite.player = self.player
            self.coin_list.add(coin_sprite)