import pygame
WIDTH=1000
HEIGHT=800
TITLE="space invaders"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption((TITLE))
background=pygame.image.load("pygameprojects\\bluespacepg.png")
yellowship=pygame.image.load("pygameprojects\\yellowship.png")
redship=pygame.image.load("pygameprojects\\redship.png")
 
class Ship(pygame.sprite.Sprite):
    def __init__(self,image,x,y,angle):
        super().__init__()
        self.image=pygame.transform.scale(image,(70,70))
        self.image=pygame.transform.rotate(self.image,(angle))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
yship=Ship(yellowship,250,400,90)
rship=Ship(redship,750,400,-90)
sprite=pygame.sprite.Group()
sprite.add(yship)
sprite.add(rship)

rship_bullets=[]
yship_bullets=[]
yship_health=10
rship_health=10
def drawbullets():
    global rship_bullets
    global yship_bullets,yship_health,rship_health
    for bullet in yship_bullets:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x=bullet.x+5
        if bullet.left>1000:
            yship_bullets.remove(bullet)
        elif bullet.colliderect(rship):
            yship_bullets.remove(bullet)
            rship_health=rship_health-1
    for bullet in rship_bullets:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x=bullet.x-5
        if bullet.right<0:
            rship_bullets.remove(bullet)
        elif bullet.colliderect(yship):
            rship_bullets.remove(bullet)
            yship_health=yship_health-1
run=True
while run==True:
    screen.blit(background,(0,0))
    sprite.draw(screen)
    drawbullets()
    pygame.draw.line(screen,"white",(500,0),(500,800),5)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_z:
                bullet=pygame.Rect(yship.rect.right,yship.rect.top+30,15,5)
                yship_bullets.append(bullet)
            if event.key==pygame.K_m:
                bullet=pygame.Rect(rship.rect.left,rship.rect.top+30,15,5)
                rship_bullets.append(bullet)
    key_pressed=pygame.key.get_pressed()
    if key_pressed[pygame.K_a]:
        yship.rect.x=yship.rect.x-2
    if key_pressed[pygame.K_d]:
        yship.rect.x=yship.rect.x+2
    if key_pressed[pygame.K_s]:
        yship.rect.y=yship.rect.y+2
    if key_pressed[pygame.K_w]:
        yship.rect.y=yship.rect.y-2
    if key_pressed[pygame.K_UP]:
        rship.rect.y=rship.rect.y-2
    if key_pressed[pygame.K_DOWN]:
        rship.rect.y=rship.rect.y+2
    if key_pressed[pygame.K_LEFT]:
        rship.rect.x=rship.rect.x-2 
    if key_pressed[pygame.K_RIGHT]:
        rship.rect.x=rship.rect.x+2
    
    if yship.rect.left<0:
        yship.rect.left=0
    if yship.rect.right>500:
        yship.rect.right=500
    if yship.rect.top<0:
        yship.rect.top=0
    if yship.rect.bottom>800:
        yship.rect.bottom=800

    if rship.rect.left<500:
        rship.rect.left=500
    if rship.rect.right>1000:
        rship.rect.right=1000
    if rship.rect.top<0:
        rship.rect.top=0
    if rship.rect.bottom>800:
        rship.rect.bottom=800
    pygame.display.update()

    

