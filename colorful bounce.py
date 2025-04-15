import pygame
import random
pygame.init()
sprite_color_change_event=pygame.userevent+1
background_color_change_event=pygame.userevent+2
blue=pygame.Color('blue')
lightblue=pygame.color('lightblue')
darkblue=pygame.color('darkblue')
yellow=pygame.color('yellow')
magenta=pygame.color('magenta')
orange=pygame.color('orange')
white=pygame.color('white')
class Sprite(pygame.sprite.Sprite):
    def _init_(self,color,height,width):
      super()._init_()
      self.image=pygame.Surface([width,height])
      self.image.fill(color)
      self.rect=self.image.get_rect()
      self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
      self.rect.move_ip(self.velocity)
      boundary_hit=False
      if self.rect.left<=0 or self.rect.right>=500:
        self.velocity[0]=-self.velocity[0]
        boundary_hit=True
      if self.rect.top<=0 or self.rect.bottom>=400:
         self.velocity[1]=-self.velocity[1]
         boundary_hit=True
      if boundary_hit:
        pygame.event.post(pygame.event.Event(sprite_color_change_event))
        pygame.eventpost(pygame.event.Event(background_color_change_event))
    def change_color(self):
      self.image.fill(random.choice([yellow,magenta,orange,white]))
def change_background_color():
  global bg_color 
  bg_color=random.choice([blue,lightblue,darkblue])
all_sprites_list=pygame.sprite.Group()
sp1=Sprite(white,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)
all_sprites_list.add(sp1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Colorful Bounce")
bg_color=blue
screen.fill(bg_color)
exit=False
clock=pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        exit=True
      elif event.type==sprite_color_change_event:
        sp1.change_color()
      elif event.type==background_color_change_event: