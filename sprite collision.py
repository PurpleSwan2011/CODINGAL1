import pygame
import random
screen_width,screen_height=500,400
movement_speed=5
font_size=72
pygame.init()
background_image=pygame.transform.scale(pygame.image.load("R.jpg"),(screen_width,screen_height))
font=pygame.font.SysFont("times new roman",font_size)
class Sprite(pygame.sprite.Sprite):
    def init(self,color,height,width):
      super().__init__()
      self.image=pygame.Surface([width,height])
      self.image.fill(pygame.Color('dodgerblue'))
      pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    def move(self,x_change,y_change):
      self.rect.x=max(
          min(self.rect.x+x_change,screen_width-self.rect.width),0)
      self.rect.y=max(
          min(self.rect.y+y_change,screen_width-self.rect.width),0)
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_captions("sprite collision")
all_sprites=pygame.sprite.Group()
sprite1=Sprite(pygame.Color('black'),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0,screen_width-sprite1.rect.width),random.randint(
    0,screen_height-sprite1.rect.height)
all_sprites.add(sprite1)
sprite2=Sprite(pygame.Color('red'),20,30)
sprite2.rect.x,sprite1.rect.y=random.randint(
    0,screen_width-sprite1.rect.width),random.randint(
    0,screen_height-sprite1.rect.height)
all_sprites.add(sprite2)
running,won=True,False
clock=pygame.time.Clock()
while running:
  for event in pygame.event.get():
    if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_x):
      running=False
  if not won:
    keys=pygame.key.get_pressed()
    x_change=(keys[pygame.k_right]-keys[pygame.k_left])*movement_speed
    y_change=(keys[pygame.k_down]-keys[pygame.k_up])*movement_speed