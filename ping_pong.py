from pygame import *
from time import monotonic
import random
'''Необхідні класи'''
 
# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        self.height = height
        self.wight = wight
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
Player1 = Player("racket.png",50,250,5,25,50)
Player2 = Player("racket.png",win_width-50,250,5,25,50)

Ball = GameSprite("tenis_ball.png",200,200,3,50,50)

#прапорці, що відповідають за стан гри
mixer.init()
mixer.music.load("katu.mp3")
mixer.music.play()
font.init()
bonus = 0
sc1x = 0
sc2x = 0
sc1 = "0"
sc2 = "0"
font1 = font.Font(None,30)
score1 = font1.render(sc1,True,(0,0,0))
score2 = font1.render(sc2,True,(0,0,0))
udarh = win_height - Ball.height
udarw = win_width - Ball.wight
game = True
finish = False
clock = time.Clock()
gift = GameSprite("tenis_ball.png",2000,200,3,50,50)
x = 5
y = 5
t = monotonic()
cr = 0
bonus1 = 0
bonus2 = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if Ball.rect.x >= udarw:
        x *= -1
        sc1x += 1
        sc1 = str(sc1x)
        score1 = font1.render(sc1,True,(0,0,0))
    if Ball.rect.x <= 0:
        x *= -1
        sc2x += 1
        sc2 = str(sc2x)
        score2 = font1.render(sc2,True,(0,0,0))

    if Ball.rect.y <= 0:
        y *= -1
    if Ball.rect.y >= udarh:
        y *= -1
    if monotonic() - t > 10:
        t = monotonic()
        xfgift = random.randint(1,2)
        if xfgift == 1:
            xgift = 50
        if xfgift == 2:
            xgift = win_width - 50
        ygift = random.randint(0,450)
        gift = GameSprite("tenis_ball.png",xgift,ygift,3,50,50)
        
    Ball.rect.x += x
    Ball.rect.y += y
    
    if sprite.collide_rect(Ball,Player1):
        x *= -1
    if sprite.collide_rect(Ball,Player2):
        x *= -1
    if sprite.collide_rect(Player1,gift):
        bonus1 += 50
        gift.rect.x += 2000
    if sprite.collide_rect(Player2,gift):
        bonus2 += 50
        gift.rect.x += 2000
    if finish != True:
        window.fill(back)
        Player1.reset()
        Player1.update_l()
        Player2.reset()
        Ball.reset()
        Player2.update_r()
        gift.reset()
        window.blit(score1,(50,50))
        window.blit(score2,(win_width - 50,50))
    display.update()
    clock.tick(60)
