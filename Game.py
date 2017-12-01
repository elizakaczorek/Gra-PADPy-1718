
import pygame
import os

from Constants_Objects import *
from Objects_classes import *
from Worlds import *
from Players import *

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.mouse.set_visible(False)

def game_over():
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(BLACK)
    pygame.display.set_caption("New Mario")

    font1 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
    text1 = font1.render("Game over", False, (255, 0, 0))
    screen.blit(text1, (230,280))
    
    pygame.display.update()
    pygame.mixer.init()
    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/game_over.wav"))
    Sound.play()

    while 1:
        for event in pygame.event.get(): 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE or event.key==pygame.K_SPACE:
                    game_menu()
            elif event.type == pygame.QUIT:
                quit()

def lives(lives):
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(BLACK)
    pygame.display.set_caption("New Mario")

    font1 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
    text1 = font1.render(str(lives)+" lives left", False, (255, 0, 0))
    screen.blit(text1, (180,280))

    pygame.display.update()
    pygame.time.wait(1000)  

def win(score):
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(BLACK)
    pygame.display.set_caption("New Mario")

    pygame.mixer.init()
    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/win.wav"))
    Sound.play()

    font1 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
    text1 = font1.render("You win", False, (255, 0, 0))
    text2 = font1.render("Your score : ", False, (255, 0, 0))
    text3 = font1.render(str(score), False, (255, 0, 0))
    screen.blit(text1, (270,150))
    screen.blit(text2, (180,250))
    screen.blit(text3, (400,350))

    pygame.display.update()
    pygame.time.wait(3000) 
    game_menu()   

def how_to_play():
    screen = pygame.display.set_mode([screen_width, screen_height])
    game_menu_image =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG.png")).convert() 
    game_menu_image = pygame.transform.scale(game_menu_image, (900,600))
    screen.blit(game_menu_image, (0,0))
    pygame.display.set_caption("New Mario")
    
    font1 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
    text1 = font1.render("How to play", False, (255, 0, 0))
    screen.blit(text1, (200,25))
    
    items_sheet = pygame.image.load(os.path.join(ROOT_PATH,"images/Button.png")).convert() 
    def get_image(x, y, width, height, a, b, color=BUT, sheet=items_sheet):
        image = pygame.Surface([width, height]).convert()
        image.blit(sheet, (0, 0), (x, y, width, height)) 
        image = pygame.transform.scale(image, (a,b))
        image.set_colorkey(color) 
        return image
    
    font2 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/BADABB__.TTF"), 50)
    but1 = get_image(189,2495,195,195,70,70)
    but2 = get_image(189,2710,195,195,70,70)
    but3 = get_image(2142,99,195,195,70,70)
    but4 = get_image(166,432,434,189,140,70)

    screen.blit(but1,(150,130))
    screen.blit(but2,(150,230))
    screen.blit(but3,(150,330))
    screen.blit(but4,(115,430))

    t_but1 = font2.render("Move right",False,(255,255,255))
    t_but2 = font2.render("Move left",False,(255,255,255))
    t_but3 = font2.render("Jump",False,(255,255,255))
    t_but4 = font2.render("Shoot",False,(255,255,255))
    
    screen.blit(t_but1,(300,135))
    screen.blit(t_but2,(300,235))
    screen.blit(t_but3,(300,335))
    screen.blit(t_but4,(300,435))

    pygame.display.update()
    
    while 1:
        for event in pygame.event.get(): 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                game_menu()

def settings():
    file = open(os.path.join(ROOT_PATH,"other_data/settings.txt"),"r")
    lines_list = file.readlines()
    player_choice = int(lines_list[0][0])
    bullet_speed = int(lines_list[1][0])
    lives_no = int(lines_list[2][0])
    file.close()

    active_button = 0
    options_no = 3
    pygame.mixer.init()
    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/menu_click.wav"))
    while 1:
        for event in pygame.event.get(): 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                file = open(os.path.join(ROOT_PATH,"other_data/settings.txt"), "w")
                new_param = [player_choice,bullet_speed,lives_no]
                for i in range(len(new_param)):    
                    lines_list[i] = str(new_param[i]) + lines_list[i][1:]
                file.write(''.join(lines_list))
                file.close()
                game_menu()
            if event.type == pygame.KEYDOWN:
                Sound.play()
                if event.key == pygame.K_DOWN:
                    active_button = (active_button + 1) % options_no
                if event.key == pygame.K_UP:
                    active_button = (active_button - 1) % options_no
                if event.key == pygame.K_RIGHT:
                    if active_button == 0:
                        player_choice = (player_choice + 1) % 2
                    elif active_button == 1:
                        if bullet_speed < 9:
                            bullet_speed += 1
                    elif active_button == 2:
                        if lives_no < 5:
                            lives_no += 1
                if event.key == pygame.K_LEFT:
                    if active_button == 0:
                        player_choice = (player_choice - 1) % 2
                    elif active_button == 1:
                        if bullet_speed > 4:
                            bullet_speed -= 1
                    elif active_button == 2:
                        if lives_no >1:
                            lives_no -= 1

        screen = pygame.display.set_mode([screen_width, screen_height])
        game_menu_image =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG.png")).convert() 
        game_menu_image = pygame.transform.scale(game_menu_image, (900,600))
        screen.blit(game_menu_image, (0,0))
        pygame.display.set_caption("New Mario")

        font = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 30)
        text = font.render("Settings", False, (255, 255, 0))
        screen.blit(text, (150,50))
                
        font = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/BADABB__.TTF"), 50)
        option_names = ["Player: ", "Bullet speed: ", "Lives: "]
        option_values = ['', str(bullet_speed), str(lives_no)]
        options = [0] * len(option_names)
        for i in range(0, len(options)):
            options[i] = font.render(option_names[i], False, (0, 0, 0))    
            screen.blit(options[i], (150, 150+100*i))
            screen.blit( font.render(option_values[i], False, (0,0,0)), (450,150+100*i))
 
        pygame.draw.circle(screen, (0, 0, 0), (110, 175+100*active_button), 10)  

        image = pygame.image.load(os.path.join(ROOT_PATH,"images/players/P"+str(player_choice+1)+"_Idle.png")).convert()
        image.set_colorkey(BLACK) 
        screen.blit(image, (430,110))
    
        arr_r = pygame.image.load(os.path.join(ROOT_PATH,"images/arr_r.png")).convert()
        arr_l = pygame.image.load(os.path.join(ROOT_PATH,"images/arr_l.png")).convert()
        arr_r.set_colorkey(WHITE)
        arr_l.set_colorkey(WHITE)

        screen.blit(arr_l, (410,170))
        screen.blit(arr_l, (410,270))
        screen.blit(arr_l, (410,370))
        screen.blit(arr_r, (505,170))
        screen.blit(arr_r, (505,270))
        screen.blit(arr_r, (505,370))
        
        pygame.display.update()           
    

def game_menu():
    active_button = 0
    pygame.mixer.init()
    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/menu_click.wav"))
    while 1:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN:
                Sound.play()
            
                if event.key == pygame.K_DOWN:
                    active_button = (active_button + 1) % 4
                if event.key == pygame.K_UP:
                    active_button = (active_button - 1) % 4
                if event.key == pygame.K_SPACE:
                    
                    if active_button == 0:
                        main()
                    elif active_button == 1:
                        settings()
                    elif active_button == 2:
                        how_to_play()
                    elif active_button == 3:
                        quit()

                

        screen = pygame.display.set_mode([screen_width, screen_height])
        game_menu_image =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG.png")).convert() 
        game_menu_image = pygame.transform.scale(game_menu_image, (900,600))
        screen.blit(game_menu_image, (0,0))
        pygame.display.set_caption("New Mario")
        
        font1 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
        text1 = font1.render("New Super Mario", False, (255, 0, 0))
        font2 = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 50)
        text2 = font2.render("New Super Mario", False, (255, 255, 0))
        screen.blit(text1, (55,150))
        screen.blit(text2, (60,155))
        
        font = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/The Messenger.ttf"), 30)
        button_names = ["Play", "Settings", "How to play", "Quit"]
        buttons = [0] * 4
        for i in range(0, len(buttons)):
            buttons[i] = font.render(button_names[i], False, (0, 0, 0))    
            screen.blit(buttons[i], (350, 250+70*i)) 
        
        pygame.draw.circle(screen, (0, 0, 0), (300, 270+70*active_button), 10)
        pygame.display.update()           


def main():
    """ Main Program """
    pygame.display.set_caption("New Mario")
 
    file = open(os.path.join(ROOT_PATH,"other_data/settings.txt"),"r")
    lines_list = file.readlines()
    player_choice = int(lines_list[0][0])
    bullet_speed = int(lines_list[1][0])
    lives_no = int(lines_list[2][0])
    file.close()

    player = Player(player_choice, lives_no)
    bullets = pygame.sprite.Group()

    world_list = []
    world_list.append(World_1(player))
    world_list.append(World_2(player))
    world_list.append(World_3(player)) 

    current_world_no = 0
    current_world = world_list[current_world_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_world
 
    player.rect.x = 250
    player.rect.y = screen_height - player.rect.height - 70
    active_sprite_list.add(player)
 
    done = False
 
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(ROOT_PATH,"sounds/melody.wav"))
    pygame.mixer.music.play(loops = -1)

    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                done = True 
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/jump.wav"))
                    Sound.play()
                    player.jump()
                if event.key == pygame.K_SPACE:
                    Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/shoot.wav"))
                    Sound.play()
                    if player.direction == "R":
                        bullets.add(Bullet("R", player.rect.midright, current_world.world_shift, bullet_speed))
                    else:
                        bullets.add(Bullet("L", player.rect.midleft, current_world.world_shift, bullet_speed))
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        active_sprite_list.update() 
        current_world.update()

        # World moving 
        if current_world.world_shift == 0:  
            if player.rect.left < 0:
                player.rect.left = 0
            elif player.rect.x > 450:
                diff = player.rect.x - 450
                player.rect.x = 450
                current_world.shift_world(-diff) 
        elif current_world.world_shift == current_world.world_limit + 900: 
            if player.rect.right > 900:
                player.rect.right = 900
            elif player.rect.x < 450:
                diff = 450 - player.rect.x
                player.rect.x = 450
                current_world.shift_world(diff) 
        else:
            if player.rect.x > 450:
                diff = player.rect.x - 450
                current_world.shift_world(-diff)
                player.rect.x = 450
                if current_world.world_shift < current_world.world_limit + 900:
                    current_world.world_shift = current_world.world_limit + 900
                    player.rect.x = 450 + diff
            elif player.rect.x < 450:
                diff = 450 - player.rect.x
                current_world.shift_world(diff)
                player.rect.x = 450
                if current_world.world_shift > 0: 
                    current_world.world_shift = 0
                    player.rect.x = 450 - diff
       
        enemy_hit_list = pygame.sprite.spritecollide(player, current_world.enemy_list, False)
        for enemy in enemy_hit_list:
            player.rect.right = enemy.rect.left
            player.lives -= 1
            Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/life_lost.wav"))
            Sound.play()
        
            if player.direction == "R":
                for i in range(11,21):
                    player.image = player.walking_right[i]
                    current_world.draw(screen)
                    active_sprite_list.draw(screen)
                    pygame.display.flip()
                    pygame.time.wait(10)
            else:
                for i in range(11,21):
                    player.image = player.walking_left[i]
                    current_world.draw(screen)
                    active_sprite_list.draw(screen)
                    screen.blit(player.walking_left[i], (player.rect.x,player.rect.y))
                    pygame.display.flip()
                    pygame.time.wait(10)
            if player.lives == 0:
                pygame.time.wait(3000)
                pygame.mixer.quit()
                game_over()

            else:
                pygame.time.wait(500)
                lives(player.lives)
                
                if current_world.world_shift < -4050:
                    player.rect.x = 450
                    player.rect.bottom = 190
                    current_world.shift_world(-current_world.world_shift-4050)  
                else:
                    current_world.shift_world(-current_world.world_shift)   
                    player.rect.bottom = 530

                pygame.time.wait(500)  
            
        for enemy in current_world.enemy_list:
            if pygame.sprite.spritecollide(enemy, bullets, True):
                Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/enemy_death.wav"))
                Sound.play()
                current_world.enemy_list.remove(enemy)
                player.score += 5
                player.coins += 5

        if player.rect.y > screen_height:
            Sound = pygame.mixer.Sound(os.path.join(ROOT_PATH,"sounds/fell_down.wav"))
            Sound.play()
            player.lives -= 1
            if player.lives == 0:
                pygame.time.wait(3000)
                pygame.mixer.quit()
                game_over()
            else:
                pygame.time.wait(500)
                lives(player.lives)
                
                if current_world.world_shift < -4050:
                    player.rect.x = 450
                    player.rect.bottom = 190
                    current_world.shift_world(-current_world.world_shift-4050)  
                else:
                    current_world.shift_world(-current_world.world_shift)   
                    player.rect.bottom = 530
                pygame.time.wait(500)             
                
        for bullet in bullets:
            bullet.update(current_world.world_shift)   
            if bullet.rect.x > 920 or bullet.rect.x < -20 :
                bullets.remove(bullet)    

        current_position = - player.rect.x + current_world.world_shift 
        if current_position < current_world.world_limit + 120 - 63/2 :
            if current_world_no < len(world_list)-1:
                player.rect.x = 250
                current_world_no += 1
                current_world = world_list[current_world_no]
                player.level = current_world
                
                pygame.mixer.init()

                if current_world_no == 1:
                    pygame.mixer.music.load(os.path.join(ROOT_PATH,"sounds/melody2.wav"))
                elif current_world_no == 2:
                    pygame.mixer.music.load(os.path.join(ROOT_PATH,"sounds/melody3.wav"))

                pygame.mixer.music.play(loops = -1)
            else:
                win(player.score)
                pygame.mixer.quit()

        current_world.draw(screen)
        active_sprite_list.draw(screen)

        for bullet in bullets:
            screen.blit(bullet.image, bullet)
        
        font = pygame.font.Font(os.path.join(ROOT_PATH,"other_data/BADABB__.TTF"), 50)
        text = font.render("Coins: " + str(player.coins), False, (255, 0, 0))
        screen.blit(text, (15,10))
        text = font.render("Lives: " + str(player.lives), False, (255, 0, 0))
        screen.blit(text, (350,10))
        text = font.render("Total Score: " + str(player.score), False, (255, 0, 0))
        screen.blit(text, (600,10))

        clock.tick(60)
        pygame.display.flip()
    
    pygame.mixer.quit()
    game_menu()
 
if __name__ == "__main__":
    pygame.init()
    game_menu()

