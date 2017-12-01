import pygame
from Constants_Objects import *

class Platform(pygame.sprite.Sprite): 
    def __init__(self, platform):  
        super().__init__()
        image = pygame.image.load(platform[0]).convert_alpha() 
        self.image = pygame.transform.scale(image, platform[1])
        self.rect = self.image.get_rect()

class Coins(pygame.sprite.Sprite): 
    def __init__(self, coin): 
        super().__init__()
        image = pygame.image.load(coin[0]).convert_alpha() 
        self.image = pygame.transform.scale(image, coin[1])
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, file_name1, file_name2, side, min_px=-100000, max_px=100000): 
        super().__init__()

        self.max_px = max_px
        self.min_px = min_px

        self.world_shift = 0        
        if side == "R":      
            self.change_x = 3
        else:
            self.change_x = -3
        self.change_y = 1

        self.side = side
        
        self.walking_right = []
        self.walking_left = []
        
        def enemy_image(file_name, color):
            image = pygame.image.load(file_name).convert_alpha() 
            image.set_colorkey(color) 
            image = pygame.transform.scale(image, (50,50))
            self.walking_left.append(image)
            image = pygame.transform.flip(image, True, False)
            self.walking_right.append(image)
        
        enemy_image(file_name1, BLACK)
        enemy_image(file_name2, BLACK)

        self.which_pic = 0
        if side == "R":
            self.image = self.walking_right[self.which_pic]
        elif side == "L":
            self.image = self.walking_left[self.which_pic]

        self.rect = self.image.get_rect()

    def update(self, world_shift):
        self.rect.x = self.rect.x + self.change_x 
        self.world_shift = world_shift
        
        if self.rect.left < self.min_px + world_shift: 
            self.rect.left = self.min_px + world_shift
            self.change_x = -self.change_x
            self.side = "R"
        elif self.rect.right > self.max_px + world_shift: 
            self.rect.right = self.max_px + world_shift
            self.change_x = -self.change_x
            self.side = "L"
        
        self.which_pic = (self.which_pic + 1) % 10
        if self.which_pic < 5 :  pos = 0
        else: pos = 1
        if self.side == "R":
            self.image = self.walking_right[pos]
        elif self.side == "L":
            self.image = self.walking_left[pos]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, side, position, world_shift, bullet_speed): 
        super().__init__()

        if side == "R":      
            self.change_x = bullet_speed
        else:
            self.change_x = -bullet_speed
        self.world_shift = world_shift 
        self.side = side

        image = pygame.image.load(BULLET).convert_alpha()
        image.set_colorkey(BLUE) 
        image = pygame.transform.scale(image, (50,50))
        
        if side == "R":
            self.image = image
        elif side == "L":
            image = pygame.transform.flip(image, True, False)
            self.image = image
        
        position = (position[0], position[1]+20)
        self.rect = self.image.get_rect(center=position)

    def update(self, world_shift):
        self.rect.x = self.rect.x + self.change_x - (self.world_shift - world_shift)
        self.world_shift = world_shift
        
