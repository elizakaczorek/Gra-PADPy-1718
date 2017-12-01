import pygame
from Constants_Objects import *
from Game import *

class Player(pygame.sprite.Sprite):
 
    def __init__(self, player_choice, lives_no):
        super().__init__()
 
        self.change_x = 0
        self.change_y = 0
        
        self.walking_left = []
        self.walking_right = []
 
        self.direction = "R"
        
        self.lives = lives_no
        self.score = 0
        self.coins = 0
 
        self.level = None 

        def player_image(file_name, color):
            image = pygame.image.load(file_name).convert()
            image.set_colorkey(color) 
            self.walking_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.walking_left.append(image)
        
        pc = str(player_choice+1)

        for i in range(1,9):
            player_image(os.path.join(ROOT_PATH,"images/players/P"+pc+"_Run_"+str(i)+".png"), BLACK)

        player_image(os.path.join(ROOT_PATH,"images/players/P"+pc+"_Idle.png"), BLACK)  # stillness - 8
        player_image(os.path.join(ROOT_PATH,"images/players/P"+pc+"_jump_up.png"), BLACK)
        player_image(os.path.join(ROOT_PATH,"images/players/P"+pc+"_jump_down.png"), BLACK)
        
        for i in range(10):
            player_image(os.path.join(ROOT_PATH,"images/players/P"+pc+"_Dead_"+str(i)+".png"), BLACK)
        
        self.image = self.walking_right[8]  
        self.rect = self.image.get_rect()
 
    def update(self):
        self.gravity()
        self.rect.x += self.change_x

        position = self.rect.x + self.level.world_shift
        if self.direction == "R":  
            if self.change_x == 0:
                self.image = self.walking_right[8]  
            elif self.change_y < -1:   
                self.image = self.walking_right[9]
            elif self.change_y > 1:  
                self.image = self.walking_right[10]
            else:
                which_im = (position // 25) % (len(self.walking_right)-13) # thanks to that , position of player does not change each loop
                self.image = self.walking_right[which_im]
        else:
            if self.change_x == 0:
                self.image = self.walking_left[8] 
            elif self.change_y < -1:  
                self.image = self.walking_left[9]
            elif self.change_y > 1:  
                self.image = self.walking_left[10]
            else:
                which_im = (position // 25) % (len(self.walking_left)-13)
                self.image = self.walking_left[which_im] 
 
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in platform_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
    
        self.rect.y += self.change_y

        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in platform_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            self.change_y = 0

        coin_hit_list = pygame.sprite.spritecollide(self, self.level.coins_list, True)
        for c in coin_hit_list:
            self.score += 1
            self.coins += 1
            Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/coins.wav"))
            Sound.play()

        if self.coins >= 100:
            self.lives += 1
            self.coins -= 100
    
    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1 
        else:
            self.change_y += 0.3
 
    def jump(self):
        self.rect.y += 1
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) 
        self.rect.y -= 1
 
        if len(platform_hit_list) > 0: 
            top_touch = False
            for block in platform_hit_list:
                if self.rect.bottom == block.rect.top:
                    top_touch = True
            if top_touch == True:
                self.change_y = -10
 
    def go_left(self):
        self.change_x = -5
        self.direction = "L"
 
    def go_right(self):
        self.change_x = 5
        self.direction = "R"
 
    def stop(self):
        self.change_x = 0

