import pygame
from Constants_Objects import *
from Objects_classes import *

class World():
    def __init__(self, player):
        self.platform_list = None
        self.enemy_list = None
        self.coins_list = None
        self.background = None
 
        self.world_shift = 0
        self.world_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.player = player
 
    def update(self):
        self.platform_list.update()
        self.enemy_list.update(self.world_shift)
        self.coins_list.update()
 
    def draw(self, screen):
        screen.blit(self.background, (0,0)) 

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.coins_list.draw(screen)
 
    def shift_world(self, shift_x):
        self.world_shift += shift_x
 
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        
        for coin in self.coins_list:
            coin.rect.x += shift_x

class World_1(World):
    def __init__(self, player):
        World.__init__(self, player)
        
        image  =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG1.png")).convert() 
        self.background = pygame.transform.scale(image, (900,600))
        self.world_limit = - 9000
           
        level_platforms = [ [PLAT1, 0, 530]] + [[PLAT2, 70*i, 530] for i in range(1,50)] + [ [PLAT3, 3500,530], # floor 1
                  [BLOCK, 600, 360],  [BLOCK, 780, 360], [CRATE, 830, 360], [CRATE, 880, 190], [BLOCK, 880, 360], [CRATE, 930, 360], 
                  [BLOCK, 980, 360], 
                  [BUSH1, 1300, 475], [BUSH2,1700, 480]] + [[BLOCK,1950+50*i,360] for i in range(10)] + [
                  [CRATE,2600,190],[CRATE,2650,190],[CRATE,2700,190],[CRATE,3000,190],[CRATE,3050,190],[CRATE,3100,190],[BLOCK,3300,190],
                  [CRATE,3350,190],[BLOCK,3400,190], 
                  [CRATE,2830,360],
                  [PLAT1, 3900, 530]] + [[PLAT2, 3900+70*i, 530] for i in range(1,25)] + [ [PLAT3, 5650,530],
                  [BLOCK,4100,360]] +[[CRATE,4350 +i*50,190] for i in range(5)] + [ [BLOCK,4850,360], [BUSH2,5090,480],
                  [BLOCK,5300,360],[BLOCK,5350,310],[BLOCK,5400,260],[BLOCK,5450,210]]+[[BLOCK,5500+50*i,210] for i in range(6)] + [
                  [PLAT1, 5850, 530], [PLAT2, 5920, 530], [PLAT3, 5990,530], [PLAT1, 6190, 530], [PLAT2, 6260, 530], [PLAT3, 6330,530],
                  [CRATE,6700,190],[CRATE,6950,190]
                  ] + [[BLOCK,6400+50*i, 360] for i in range(20) ] + [[PLAT1,7040,530]]+[[PLAT2,7110+70*i,530] for i in range(26)]+[
                  [PLAT3,8930,530]]+[[BLOCK,8550,480-50*i] for i in range(8)] + [[BLOCK,8500,480-50*i] for i in range(7)] + [
                  [BLOCK,8450,480-50*i] for i in range(6)] +[[BLOCK,8400,480-50*i] for i in range(5)]+[[BLOCK,8350,480-50*i] for i in range(4)]+[
                  [BLOCK,8300,480-50*i] for i in range(3)]+[[BLOCK,8250,480-50*i] for i in range(2)]+[ [BLOCK,8200,480],
                  [CRATE,7800,360],[CRATE,7800,190],[CRATE,7950,360],[CRATE,7950,190],
                  [NEXT_LEVEL,8870,465]
                 ]

        for platform in level_platforms:
            block = Platform(platform[0]) 
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            self.platform_list.add(block)

        level_coins = [[MUSH1, 900, 330], [MUSH2, 935, 330], [MUSH1,950,500],[MUSH1,990,500], [MUSH2,1025,500], [MUSH2,1450,500],
                       [MUSH2,1500,500], [MUSH1, 2060,330],[MUSH2,2080,330], [MUSH1,2120,330],[MUSH1,3025,160],[MUSH2,3045,160],
                       [MUSH1,2630, 500],[MUSH1,3950,500],[MUSH2,4000,500]] + [[MUSH1,4400+25*i,160] for i in range(7)] + [
                       [MUSH2,4500+25*i,500] for i in range(7)] + [[MUSH1,5470+i*35,180] for i in range(9)] + [[MUSH1,5515,500],[MUSH2,5555,500],
                       [MUSH1,6707,160],[MUSH2,6957,160],[MUSH2,6750,330],[MUSH2,6985,330]]+[[MUSH1,7120+i*37,500] for i in range(6)] + [
                       [MUSH2,8715,500],[MUSH2,8745,500],[MUSH1,7800,330],[MUSH2,7800,160],[MUSH1,7950,330],[MUSH2,7950,160],
                       [MUSH1,885,160]]+[[MUSH2,3315+30*i,500] for i in range(8)]+[
                       ]
        for c in level_coins:
            coin = Coins(c[0]) 
            coin.rect.x = c[1]
            coin.rect.y = c[2]
            self.coins_list.add(coin)
        
        level_enemies = [ [ENEMY1,1300,480,"L",-100000,1300], [ENEMY1,1370,480,"L",-100000,1700], [ENEMY4,2430,310,"L",1950,2450],
                  [ENEMY3,6000,300,"L",5700,6350],[ENEMY4,1800,480,"R",1780,3550],[ENEMY1,2500,480,"L",1780,3550],
                  [ENEMY3,4200,360,"R",4150,4850],[ENEMY4,4500,480,"L",3890,5090], [ENEMY1,7000,310,"L",6390,7390],
                  [ENEMY4,8100,480,"L",7025,8185],[ENEMY4,8000,480,"L",7025,8185],[ENEMY1,7200,480,"R",7025,8185]
                   ]

        for e in level_enemies:
            enemy = Enemy(e[0][0],e[0][1], e[3])
            enemy.rect.x = e[1]
            enemy.rect.y = e[2]
            enemy.min_px = e[4]
            enemy.max_px = e[5]
            self.enemy_list.add(enemy)
 
class World_2(World):
 
    def __init__(self, player):
        World.__init__(self, player)
        image  =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG2.png")).convert() 
        self.background = pygame.transform.scale(image, (900,600))
        
        self.world_limit = - 9000
           
        level_platforms = [ [D1, 0, 530]] + [[D2, 70*i, 530] for i in range(1,11)] + [ [D3, 770,530], [CACTUS1,20,420],
                  [STONEBLOCK,475,360],[STONEBLOCK,525,360],[STONEBLOCK,575,360], [D1, 1050, 530]] + [[D2, 1050+70*i, 530] for i in range(1,30)] + [[D3,3150,530],
                  [STONEBLOCK,775,190],[STONEBLOCK,825,190],[STONEBLOCK,875,190],[STONEBLOCK,925,190],[STONEBLOCK,1250,190],[STONEBLOCK,1300,190],[STONEBLOCK,1350,190],
                  [CRATE,1115,360],[CRATE,1525,360], [STONEBLOCK,3170,480],[STONEBLOCK,3120,480],[STONEBLOCK,3070,480],[STONEBLOCK,3170,430],[STONEBLOCK,3120,430],
                  [STONEBLOCK,3170,380],[CACTUS2,1745,420],[STONEBLOCK,2050,360],[STONEBLOCK,2100,310],[STONEBLOCK,2150,260],[STONEBLOCK,2200,210]] + [ 
                  [STONEBLOCK,2400+50*i,210] for i in range(1,7)] + [[CRATE,2600,360],
                  [D1, 3350, 530]] + [[D2, 3350+70*i, 530] for i in range(1,20)] + [[D3,4750,530],
                  [STONEBLOCK,3350,480],[STONEBLOCK,3400,480],[STONEBLOCK,3450,480],[STONEBLOCK,3350,430],[STONEBLOCK,3400,430],[STONEBLOCK,3350,380],[CACTUS1,3710,420],
                  [CRATE,4150,360],[CRATE,4100,360],[CRATE,4050,360],[CRATE,4000,360],[CRATE,4400,190],[CRATE,4450,190],[CRATE,4500,190],[CRATE,4550,190],
                  [STONEBLOCK,4720,360],[STONEBLOCK,4820,190],[STONEBLOCK,4870,240],[STONEBLOCK,4920,290],[STONEBLOCK,4970,340],[STONEBLOCK,5020,390],
                  [D1, 5200, 530]] + [[D2, 5200+70*i, 530] for i in range(1,25)] + [[D3,6950,530],[CACTUS1,5300,420]] + [
                  [STONEBLOCK,5800+i*120,480] for i in range(7)] + [[STONEBLOCK,5920+i*120,430] for i in range(5)]+ [[STONEBLOCK,6040+i*120,380] for i in range(3)] + [
                  [STONEBLOCK,6160,330], [CRATE,6380,190],[CRATE,6430,190],[CRATE,6480,190],[CRATE,6700,360],[CRATE,6750,360],[CRATE,6800,360],
                  [CRATE,6700,190],[CRATE,6750,190],[CRATE,6800,190],[D1, 7300, 530]] + [[D2, 7370+70*i, 530] for i in range(0,24)] + [
                  [STONED,7420,465],[CACTUS2,7830,420],[CRATE,7050,275],[CRATE,7100,275],[CRATE,7150,275],[CRATE,7200,275]
                  
                  ]+[[STONEBLOCK,8550,480-50*i] for i in range(8)] + [[STONEBLOCK,8500,480-50*i] for i in range(7)] + [
                  [STONEBLOCK,8450,480-50*i] for i in range(6)] +[[STONEBLOCK,8400,480-50*i] for i in range(5)]+[[STONEBLOCK,8350,480-50*i] for i in range(4)]+[
                  [STONEBLOCK,8300,480-50*i] for i in range(3)]+[[STONEBLOCK,8250,480-50*i] for i in range(2)]+[[STONEBLOCK,8200,480],
                  [NEXT_LEVEL,8870,465]
                 ]

        for platform in level_platforms:
            block = Platform(platform[0]) 
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            self.platform_list.add(block)

        level_coins = [[MUSH1,530,330],[MUSH2,565,330],[MUSH2,800,160],[MUSH1,830,160],[MUSH1,835,160]] +[[MUSH2,1115+40*i,500] for i in range(6)]+ [
                       [MUSH1,1125+40*i,500] for i in range(3)] + [[MUSH2,2505,180],[MUSH1,2550,180],[MUSH2,2150,230]] +[[MUSH2,2175+30*i,500] for i in range(8)]+[
                       [MUSH1,2605,330],[MUSH1,2810,500],[MUSH1,2830,500],[MUSH1,2870,500],[MUSH1,4010,330],[MUSH1,4045,330],[MUSH2,4070,330], [MUSH1,4140,500]] + [
                       [MUSH2,4405,160],[MUSH2,4445,160]]+[[MUSH1,4140+38*i,500] for i in range(6)]+[[MUSH1,5510,500],[MUSH2,5540,500],[MUSH2,6380,160],[MUSH1,6400,160],
                       [MUSH2,6420,160]]+[[MUSH2,6685+i*35,500] for i in range(7)]+ [[MUSH2,6730,160],[MUSH1,6750,160],[MUSH2,6770,160],
                       [MUSH2,6750,330],[MUSH1,6770,330],[MUSH2,6790,330],[MUSH1,8000,500],[MUSH2,8025,500],[MUSH2,7800,500]
                       ]
        for c in level_coins:
            coin = Coins(c[0]) 
            coin.rect.x = c[1]
            coin.rect.y = c[2]
            self.coins_list.add(coin)
        
        level_enemies = [ [ENEMY4,780,480,"L",120,830],[ENEMY3,1200,360,"R",1165,1525],[ENEMY4,1700,480,"L",1050,1745],[ENEMY4,3000,480,"L",1845,3070],
                          [ENEMY4,2920,480,"L",1845,3070],[ENEMY3,2500,310,"L",2175,2600],[ENEMY1,2000,480,"R",1845,3070],[ENEMY3,2700,310,"R",2650,3100],
                          [ENEMY4,3650,480,"L",3500,3710],[ENEMY4,4300,480,"L",3810,4820],[ENEMY4,5500,480,"R",5400,5800],[ENEMY4,6650,480,"R",6570,7020],
                          [ENEMY4,7790,480,"L",7530,7830],[ENEMY4,7100,225,"R",7050,7250]
                   ]

        for e in level_enemies:
            enemy = Enemy(e[0][0],e[0][1], e[3])
            enemy.rect.x = e[1]
            enemy.rect.y = e[2]
            enemy.min_px = e[4]
            enemy.max_px = e[5]
            self.enemy_list.add(enemy)

class World_3(World):
 
    def __init__(self, player):
        World.__init__(self, player)
        
        image  =  pygame.image.load(os.path.join(ROOT_PATH,"images/backgrounds/BG3.png")).convert() 
        self.background = pygame.transform.scale(image, (900,600)) 
        self.world_limit = - 9000
           
        level_platforms = [ [W1, 0, 530]] + [[W2, 70*i, 530] for i in range(1,52)] + [ [W3, 3640,530], [CRYSTAL,30,450],[ICEBOX,450,360],[ICEBOX,630,190],
                  [ICEBOX,270,190],[ICEBOX,900,190],[ICEBOX,950,190],[ICEBOX,1000,190],[ICEBOX,1050,190],[ICEBOX,1100,190],[ICEBOX,1150,190],[ICEBOX,1200,190],
                  [STONEW,730,465],[ICEBOX,1350,360],[CRYSTAL,1525,450],[ICEBOX,1800,360],[ICEBOX,1800,310],[ICEBOX,1800,260],[ICEBOX,1850,360],[ICEBOX,1900,360],
                  [ICEBOX,1950,360],[ICEBOX,1950,310],[ICEBOX,1950,260],[ICEBOX,2000,260],[ICEBOX,2050,260],[ICEBOX,2100,260],[ICEBOX,2150,260],[ICEBOX,2150,310],
                  [ICEBOX,2150,360],[ICEBOX,2200,360],[ICEBOX,2250,360],[ICEBOX,2300,360],[ICEBOX,2300,310],[ICEBOX,2300,260],
                  [ICEBOX,1550,190],[CRYSTAL,2010,450],
                  [ICEBOX,2600,360],[ICEBOX,2650,360],[ICEBOX,2600,310],[ICEBOX,2650,310],[ICEBOX,2600,260],[ICEBOX,2650,260],
                  [ICEBOX,2500,160],[ICEBOX,2550,160],[ICEBOX,2500,210],[ICEBOX,2550,210],[ICEBOX,2500,260],[ICEBOX,2550,260],
                  [ICEBOX,2600,110],[ICEBOX,2650,110],[ICEBOX,2600,60],[ICEBOX,2650,60],[ICEBOX,2600,10],[ICEBOX,2650,10]]+[[ICEBOX,2600+i*50,-40] for i in range(27)]+[
                  [ICEBOX,2800+i*50,10] for i in range(6)]+[[ICEBOX,2800+i*50,60] for i in range(6)]+[[ICEBOX,2800+i*50,360] for i in range(6)]+[
                  [ICEBOX,3050,360-i*50] for i in range(1,6)]+[[ICEBOX,3150+i*50,10] for i in range(5)]+[[ICEBOX,3150+i*50,60] for i in range(5)]+[
                  [ICEBOX,3200,110+i*50] for i in range(6)]+[[ICEBOX,3250,360],[ICEBOX,3300,360],[ICEBOX,3350,360],[ICEBOX,3350,310]]+[
                  [ICEBOX,3500,360-50*i] for i in range(5)]+[[ICEBOX,3550,360-50*i] for i in range(4)]+[[ICEBOX,3700+i*50,360] for i in range(5)] + [
                  [ICEBOX,3700+i*50,10] for i in range(5)]+[[ICEBOX,3700+i*50,60] for i in range(5)] +[[ICEBOX,4100+i*50,210] for i in range(5)]+[
                  [W1,4050,530],[W3,4120,530],[CRYSTAL,4080,450]]+[[ICEBOX,4450+i*50,210] for i in range(3)]+[[W1,4410,530],[W3,4480,530],[CRYSTAL,4440,450]]+[
                  [ICEBOX,4750+i*50,360] for i in range(7)]+[[W1,5250,530]]+[[W2,5320+i*70,530] for i in range(13)]+[[W3,6180,530],
                  [STONEW,5270,465],[ICEBOX,5550,360],[CRATE,5600,360],[ICEBOX,5650,360],[CRATE,5700,360],[ICEBOX,5750,360],
                  [CRATE,5800,190],[ICEBOX,5600,190],[ICEBOX,5650,190],[CRATE,5700,190],[ICEBOX,5750,190],[ICEBOX,5850,190],[ICEBOX,5900,190],
                  [CRYSTAL,5950,450]]+[
                  [ICEBOX,6200,480-i*50] for i in range(6)]+[[ICEBOX,6320,580-i*50] for i in range(7)]+[
                  [ICEBOX,6440,580-i*50] for i in range(6)]+[[ICEBOX,6560,580-i*50] for i in range(5)]+[[ICEBOX,6680,580-i*50] for i in range(4)]+[
                  [ICEBOX,6800,580-i*50] for i in range(3)]+[[ICEBOX,6920,580-i*50] for i in range(2)]+[[ICEBOX,7040,580],
                  [W1,7250,530]]+[[W2,7320+i*70,530] for i in range(8)]+[[W3,7830,530]]+[
                  [ICEBOX,7350+i*50,360] for i in range(9)]+[[CRATE,7400+i*50,190] for i in range(7)]+[                    
                  [W1,8100,530]]+[[W2,8170+70*i,530] for i in range(12)]+[
                  ]+[[ICEBOX,8550,480-50*i] for i in range(8)] + [[ICEBOX,8500,480-50*i] for i in range(7)] + [
                  [ICEBOX,8450,480-50*i] for i in range(6)] +[[ICEBOX,8400,480-50*i] for i in range(5)]+[[ICEBOX,8350,480-50*i] for i in range(4)]+[
                  [ICEBOX,8300,480-50*i] for i in range(3)]+[[ICEBOX,8250,480-50*i] for i in range(2)]+[[ICEBOX,8200,480],
                  [THE_END,8870,465],
                 ]

        for platform in level_platforms:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            self.platform_list.add(block)

        level_coins = [[MUSH1,277,162]]+[[MUSH2,1000+i*33,162] for i in range(3)]+[[MUSH1,900+36*i,500] for i in range(4)]+ [[MUSH1,1855,332],[MUSH2,1890,332],
                       [MUSH1,1985,232],[MUSH1,2015,232],[MUSH1,2050,232],[MUSH2,2100,232],[MUSH1,2130,232],[MUSH1,2205,332],[MUSH1,2230,332],
                       [MUSH1,2607,232],[MUSH1,2640,232],[MUSH1,2515,132],[MUSH2,2557,132]]+[[MUSH1,3000-30*i,332] for i in range(6)]+[[MUSH1,3285,332],
                       [MUSH2,3255,332],[MUSH1,3300,332],[MUSH1,4110,182],[MUSH2,4145,182],[MUSH2,4190,182],[MUSH1,4250,182]]+[[MUSH1,2600+i*37,500] for i in range(5)]+[
                       [MUSH1,4800,332],[MUSH1,4838,332], [MUSH2,5607,162],[MUSH1,5635,162],[MUSH1,5671,162],[MUSH2,5750,162]]+[
                       [MUSH1,5490+i*70,502] for i in range(6)]+[[MUSH2,5520+i*68,502] for i in range(7)]+[[MUSH1,6065,502],[MUSH2,6100,502],[MUSH1,6143,502]]+[
                       [MUSH1,7315+76*i,502] for i in range(8)]+[[MUSH2,7400+59*i,502] for i in range(6)]+[[MUSH1,7405+37*i,332] for i in range(2)]+[
                       [MUSH2,7590+45*i,162] for i in range(3)]  

        for c in level_coins:
            coin = Coins(c[0]) 
            coin.rect.x = c[1]
            coin.rect.y = c[2]
            self.coins_list.add(coin)
        
        level_enemies = [[ENEMY2,1200,140,"L",900,1250],[ENEMY3,1000,360,"R",850,1300],[ENEMY3,1000,360,"L",850,1300],[ENEMY1,1450,480,"L",840,1525],
                         [ENEMY2,1900,480,"L",1605,2010],[ENEMY1,2150,480,"R",2090,3700],[ENEMY1,2550,480,"L",2090,3700],[ENEMY2,3600,480,"L",2090,3700],
                         [ENEMY2,5000,310,"L",4750,5100],[ENEMY4,5650,140,"R",5600,5950],[ENEMY1,5450,480,"R",5380,5950],[ENEMY2,5850,480,"R",5380,5950],
                         [ENEMY2,7300,480,"R",7250,7900],[ENEMY1,7800,480,"L",7250,7900]
                   ]
        for e in level_enemies:
            enemy = Enemy(e[0][0],e[0][1], e[3])
            enemy.rect.x = e[1]
            enemy.rect.y = e[2]
            enemy.min_px = e[4]
            enemy.max_px = e[5]
            self.enemy_list.add(enemy)

