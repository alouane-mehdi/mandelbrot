import pygame
import sys

class Main:
    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((1200,500))

        self.triangle_de_sierpinski = pygame.transform.scale(pygame.image.load('image/triangle_de_sierpinski.png') , (240,200))
        self.mandelbrot = pygame.transform.scale(pygame.image.load('image/mandelbrot.jpeg') , (240,200))
        self.julia = pygame.transform.scale(pygame.image.load('image/Julia.png') , (240,240))
        self.flocon_de_koch = pygame.transform.scale(pygame.image.load('image/flocon_de_koch.jpeg') , (240,200)) 
        self.burning_ship = pygame.transform.scale(pygame.image.load('image/burning_ship.png') , (240,200))

        self.rect_triangle= pygame.Rect(0,170,240,200)
        self.rect_mandelbrot = pygame.Rect(240,170,240,200)
        self.rect_julia = pygame.Rect(480,170,240,200)
        self.rect_flocon= pygame.Rect(720,170,240,200)
        self.rect_burning_ship = pygame.Rect(960,170,240,200)

        self.images = [self.triangle_de_sierpinski,self.mandelbrot,self.julia,self.flocon_de_koch,self.burning_ship]
        
    
    def display_image(self):
        x=0
        y = 170
        for i in self.images:
            self.screen.blit(i,(x,y))
            x+=240
    

    def main_pygame(self): 
        while self.running: 
            self.display_image()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_triangle.collidepoint(event.pos):
                        print("yes")
                    elif self.rect_triangle.collidepoint(event.pos):
                        print("yes")
                    elif self.rect_triangle.collidepoint(event.pos):
                        print("yes")
                    elif self.rect_triangle.collidepoint(event.pos):
                        print("yes")
                    elif self.rect_triangle.collidepoint(event.pos):
                        print("yes")
            
            pygame.display.flip()

main=Main()
main.main_pygame()

                

