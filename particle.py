import pygame
import random

class Particle:

    def __init__(self, target):

        self.tx, self.ty = target

        self.x = random.randint(-400,1400)

        self.y = random.randint(-400,1400)

        self.speed = random.uniform(0.02,0.05)

        self.size = random.randint(2,4)

        self.life = random.randint(150,255)

    def update(self):

        self.x += (self.tx-self.x)*self.speed

        self.y += (self.ty-self.y)*self.speed

    def draw(self,screen):

        surf = pygame.Surface((20,20),pygame.SRCALPHA)

        pygame.draw.circle(
            surf,
            (255,70,170,self.life),
            (10,10),
            self.size
        )

        screen.blit(
            surf,
            (self.x-10,self.y-10)
        )
