from pygame import *

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
Player2 = Player("racket.png",500,250,5,25,50)

Ball = GameSprite("tenis_ball.jpg",200,200,3,50,50)
#прапорці, що відповідають за стан гри
udarh = win_height - Ball.height
udarw = win_width - Ball.wight
game = True
finish = False
clock = time.Clock()
udarx = 0
udary = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Ball.rect.x >= udarw:
        udarx = 1
    if Ball.rect.x <= 0:
        udarx = 0
    if Ball.rect.y >= udarh:
        udary = 1
    if Ball.rect.y <= 0:
        udary = 0
    
    
    if udarx == 0:
        Ball.rect.x += Ball.speed
    if udarx == 1:
        Ball.rect.x -= Ball.speed
    if udary == 0:
        Ball.rect.y += Ball.speed
    if udary == 1:
        Ball.rect.y -= Ball.speed
    
    if sprite.collide_rect(Ball,Player1):
        udarx = 0
    if sprite.collide_rect(Ball,Player2):
        udarx = 1
    Player2.rect.y = Ball.rect.y
    if finish != True:
        window.fill(back)
        Player1.reset()
        Player1.update_l()
        Player2.reset()
        Ball.reset()
        Player2.update_r()
    display.update()
    clock.tick(60)
