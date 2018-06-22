import pygame
from pygame.locals import *
width=400
height=400
# tao khung hien thi game
display_surf = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
fps=200 # so frame tren giay
fps_clock=pygame.time.Clock()
class Snake:
    def __init__(self,r,x,y,speed):
        self.r=r
        self.x=x
        self.y=y
        self.speed=speed
    def draw(self):
        pygame.draw.circle(display_surf,(53,160,7),(0,0),10,10)
    def move(self,m):
        dx=0
        dy=0
        if self.m=="a" and m.lower()=="d": return
        if self.m=="d" and m.lower()=="a": return
        if self.m=="w" and m.lower()=="s": return
        if self.m=="s" and m.lower()=="w": return
        self.m=m.lower()
        if self.m=="a":
            dx=-speed
        elif self.m=="d":
            dx=speed
        elif self.m=="w":
            dy=-speed
        elif self.m=="s":
            dy=speed
        else:
            dx=0
            dy=0
        self.x+=dx
        self.y+=dy
class Food:
    def __init__(self,r,x,y):
        self.r=r
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.circle(display_surf,(239,232,95),(0,0),10,10)
    def Eat(self):
        if Snake.x+Snake.r>=self.x+self.r>=Snake.x-Snake.r and Snake.y+Snake.r>=self.y+self.r>=Snake.y-Snake.r:
            return True