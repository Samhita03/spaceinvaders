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
    def __init__(self,image,x,y):
        super().__init__()
        self.image=pygame.transform.scale(image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
yship=Ship(yellowship,250,400)
rship=Ship(redship,750,400)
sprite=pygame.sprite.Group()
sprite.add(yship)
sprite.add(rship)
run=True
while run==True:
    screen.blit(background,(0,0))
    sprite.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()

    

