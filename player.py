import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        
        #General setup
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        
        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("up")
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            print("down")
            self.direction.y = 1
        elif keys[pygame.K_RIGHT]:
            print("right")
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            print("left")
            self.direction.x = -1
        else:
            self.direction.x = 0
            self.direction.y = 0
       
        #print(self.direction)
    
    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
        
    
    def update(self,dt):
        self.input()
        self.move(dt)
