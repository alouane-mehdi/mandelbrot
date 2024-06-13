import pygame
import sys

class Main:
    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800,1000))
        self.OakBlock = pygame.transform.scale(pygame.image.load('image/block_07.png'), (65, 65))

        triangle_de_Sierpiński = pygame.transform.scale(pygame.image.load('image/') , (100,200))
        Mandelbrot = pygame.transform.scale(pygame.image.load('image/') , (100,200))
        Julia = pygame.transform.scale(pygame.image.load('image/Julia') , (100,200))
        flocon_de_Koch = pygame.transform.scale(pygame.image.load('image/') , (100,200)) 
        burning_ship = pygame.transform.scale(pygame.image.load('image/') , (100,200))
    

    def main_pygame(self): 
        while self.running: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False
                


