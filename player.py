import pygame

resistance = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = (30, 50)
frame_width, frame_height = 13, 19

spritesheet = pygame.image.load("platformer_game/assets/sprites/knight.png")

idle_frames = []
idle_frames_num = 4
for i in range(idle_frames_num):
    x = i * 32
    sprite_rect = pygame.Rect(x + 9, 9, frame_width, frame_height)

    frame = spritesheet.subsurface(sprite_rect)
    idle_frames.append(frame)

run_frames = []
run_frames_num = 8
for i in range(run_frames_num):
    x = i * 32
    sprite_rect = pygame.Rect(x + 9, 73, frame_width, frame_height)

    frame = spritesheet.subsurface(sprite_rect)
    run_frames.append(frame)

jump_frames = []
jump_frames_num = 8
for i in range(jump_frames_num):
    x = i * 32
    sprite_rect = pygame.Rect(x + 9, 169, frame_width, frame_height)

    frame = spritesheet.subsurface(sprite_rect)
    jump_frames.append(frame)

death_frames = []
death_frames_num = 4
for i in range(death_frames_num):
    x = i * 32
    sprite_rect = pygame.Rect(x + 9, 233, frame_width, frame_height)

    frame = spritesheet.subsurface(sprite_rect)
    death_frames.append(frame)

state_list = ["idle", "run right", "run left", "jump", "death"]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.state = 0

        self.frame_idx = 0
        self.frame_counter = 0

        self.image = idle_frames[self.frame_idx]
        self.image = pygame.transform.scale(self.image, size)
        

        self.rect = self.image.get_rect()
        self.rect.x = 100
        

        self.x_velo = 0
        self.y_velo = 0

        self.isAlive = True
        self.level = None

    def update(self, screen):

        self.updForces()
        self.updImg(screen)

        self.rect.y += self.y_velo
        
        block_collides = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_collides:
            if self.y_velo > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            
            self.y_velo = 0
            self.state = 0

        self.rect.x += self.x_velo
        block_collides = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_collides:
            if self.x_velo > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
            
            self.x_velo = 0
            self.state = 0

        enemy_collides = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemy_collides:
            self.state = 4

        if self.rect.y > 720:
            self.rect.y = 0
            self.y_velo = 0
            self.state = 0
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
                if self.state != 3:
                    self.state = 1
            else: self.x_velo = 10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if self.x_velo > -10:
                self.x_velo -= 7
                if self.state != 3:
                    self.state = 2
            else: self.x_velo = -10

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if self.y_velo != 0:
                
                pass
            else:
                self.y_velo = -20
                self.state = 3
                self.frame_idx = 0

    def updImg(self, screen):
        if self.state == 0:
            self.frame_counter += 1

            if self.frame_counter >= 30:
                self.frame_counter = 0

                self.frame_idx = (self.frame_idx + 1) % len(idle_frames)

                self.image = idle_frames[self.frame_idx]
                self.image = pygame.transform.scale(self.image, size)

        elif self.state == 1 or self.state == 2:
            self.frame_counter += 1
            if self.frame_counter >= 5:
                self.frame_counter = 0

                self.frame_idx = (self.frame_idx + 1) % len(run_frames)
                self.image = run_frames[self.frame_idx]
                self.image = pygame.transform.scale(self.image, size)
                if self.state == 2:
                    self.image = pygame.transform.flip(self.image, True, False)
        
        elif self.state == 3:
            self.frame_counter += 1
            if self.frame_counter >= 5:
                self.frame_counter = 0

                self.frame_idx = (self.frame_idx + 1) % len(jump_frames)
                self.image = jump_frames[self.frame_idx]
                self.image = pygame.transform.scale(self.image, size)

        elif self.state == 4:
            self.isAlive = False
            pygame.event.set_blocked(pygame.KEYDOWN)
            idx = 0

            for i in range(100):
                if i % 25 == 0:
                    self.image = death_frames[idx]
                    self.image = pygame.transform.scale(self.image, size)

                    idx += 1
            
            self.reset(screen)
                    
        else:
            pass

    def reset(self, screen):
        font = pygame.font.Font("platformer_game/assets/fonts/PixelOperator8.ttf")

        text = font.render("Press R to Reset", True, WHITE, None)
        text_rect = text.get_rect(center=(640, 360))
        screen.blit(text, text_rect)

        pygame.event.set_allowed(pygame.KEYDOWN)