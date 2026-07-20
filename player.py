import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, y_velocity, x_velocity):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.y_velo = y_velocity
        self.x_velo = x_velocity

    def update(self):
        self.rect.y += self.y_velo
        self.rect.x += self.x_velo

        if self.rect.y > 720:
            self.rect.y = 0
            self.y_velo = 0
            self.rect.x = 100
        


    def isCollidePlatform(self, platform):
        return not self.rect.colliderect(platform.rect)
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if self.x_velo < 10:
                self.x_velo += 10
            else: self.x_velo = 10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if self.x_velo > -10:
                self.x_velo -= 10
            else: self.x_velo = -10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if self.y_velo != 0:
                pass
            else: self.y_velo = -20
