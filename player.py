import pygame

resistance = 1

width, height = 30, 50

spritesheet = pygame.image.load("brackeys_platformer_assets/sprites/knight.png")

idle_frames = []
num_frames = 4
for i in range(num_frames):
    x = i * 32
    sprite_rect = pygame.Rect(x + 9, 9, 13, 19)

    frame = spritesheet.subsurface(sprite_rect)
    idle_frames.append(frame)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
        self.image = idle_frames[0]
        self.image = pygame.transform.scale(self.image, (150, 250))
        

        self.rect = self.image.get_rect()
        self.rect.x = 100
        

        self.x_velo = 0
        self.y_velo = 0

        self.level = None

    def update(self):

        self.updForces()

        self.rect.y += self.y_velo
        
        block_collides = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_collides:
            if self.y_velo > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            
            self.y_velo = 0

        self.rect.x += self.x_velo
        block_collides = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_collides:
            if self.x_velo > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
            
            self.x_velo = 0

        if self.rect.y > 720:
            self.rect.y = 0
            self.y_velo = 0
            self.rect.x = 100
    
    def updForces(self):
        if self.y_velo == 0:
            self.y_velo = 1
        else:
            self.y_velo += resistance

        if self.x_velo != 0:
            if self.x_velo > 0:
                self.x_velo -= resistance
            else:
                self.x_velo += resistance

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if self.x_velo < 10:
                self.x_velo += 7
            else: self.x_velo = 10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if self.x_velo > -10:
                self.x_velo -= 7
            else: self.x_velo = -10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if self.y_velo != 0:
                pass
            else: self.y_velo = -15

    def updImg(self):
        for i in range(4):
            self.image = idle_frames[i]
            self.image = pygame.transform.scale(self.image, (150, 250))