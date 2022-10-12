import pygame,time
import random
from os import path
pygame.init()
screen = pygame.display.set_mode((1200,805))
clock = pygame.time.Clock()
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound('pew.wav')
pygame.mixer.music.load('music1.ogg')
pygame.mixer.music.set_volume(0.4)
background = pygame.image.load('bground.png')
background_rect = background.get_rect(center=(600,400))
player_img = pygame.image.load('ship3.png')
meteor_img = pygame.image.load('meteor.png')
meteor_img=pygame.transform.scale(meteor_img, (100,85))
explosion=pygame.image.load('exp3.png')

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
class Player():
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.image=pygame.transform.scale(player_img, (50, 120))
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 720
        self.speedx = 4
        self.counter=0
        self.counter1=0
        self.score=0
        self.T=59
    def update(self):
        button= pygame.key.get_pressed()
        if button[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if button[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if self.rect.right > 1200:
            self.rect.right = 1200
        if self.rect.left < 0:
            self.rect.left = 0
    def draw(self):
        screen.blit(self.image,self.rect)
        
    def counts(self):
        font = pygame.font.SysFont("Verdana", 60)
        text1 = font.render(str(self.counter1), True, (0, 128, 0))
        text2=font.render('Time in sec:',True,(0,128,0))
        text3=font.render('Game Over',True,(255,255,255))
        screen.blit(text2,(400,180))
        screen.blit(text1, (775, 180))
        self.counter1=round(self.counter/60)
        if self.counter1<=self.T:
            self.counter += 1
        if self.counter1>self.T:
            screen.blit(text3, (775, 600))

class Stone(pygame.sprite.Sprite):
    def __init__(self,sc):
        super().__init__()
        self.image = meteor_img
        self.sc=sc
        self.image=pygame.transform.scale(self.image,(sc*5,sc*5))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1150)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(5,15)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 810 or self.rect.left < -25 or self.rect.right > 1220:
            self.rect.x = random.randrange(1200 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)    
    def draw(self):
        screen.blit(self.image,self.rect)
player = Player()

stones_group=pygame.sprite.Group()



Q=20
for i in range (Q):
    stone=Stone(random.randint(1,6))
    stone.update()
    stones_group.add(stone)
x,y=2000,2000
k,q,q1,s=0,0,0,0
pygame.mixer.music.play(loops=-1)
game_over=False
while True:
    print(player.T)
    if player.counter1>player.T:
        game_over=True
    clock.tick(60)
    screen.blit(background, background_rect)
    player.counts()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if q==0:
        player.update()
        if game_over==False:
            player.draw()
    stones_group.update()
    if game_over==False:
        stones_group.draw(screen)
    if player.counter1<=player.T:
        collision= pygame.sprite.spritecollide(player,stones_group,True)

    if collision:
        stone=Stone(random.randint(1,6))
        stones_group.add(stone)
        if player.counter1<=player.T:
            player.score=player.score+1
        q=1
        shoot_sound.play()
        k=1
        x1=player.rect.centerx
        y1=player.rect.centery
    if k==1 and q==1:
        s=s+1
        screen.blit(explosion,(x1,y1))
        if s==5:
            k,q,s=0,0,0
    draw_text(screen, 'Penalty=', 38, 510, 10)
    draw_text(screen, str(player.score), 38, 600, 10)
    pygame.display.update()
    
 





