import pygame
from Fractales import Julia , Mandelbrot , Sierpinski

class Main:
    def __init__(self) :
        # Initialisation des scripts de fractales
        self.julia_script = Julia()
        self.sierpinski_script = Sierpinski()
        self.mandelbrot_script = Mandelbrot()

        pygame.init()

        self.running = True
        # Création de la fenêtre
        self.screen = pygame.display.set_mode((1200, 500))

        # Chargement des images
        self.triangle_de_sierpinski = pygame.transform.scale(pygame.image.load('image/triangle_de_sierpinski.png'), (240, 200))
        self.mandelbrot = pygame.transform.scale(pygame.image.load('image/mandelbrot.jpeg'), (240, 200))
        self.julia = pygame.transform.scale(pygame.image.load('image/Julia.png'), (240, 240))
        self.flocon_de_koch = pygame.transform.scale(pygame.image.load('image/flocon_de_koch.jpeg'), (240, 200)) 
        self.burning_ship = pygame.transform.scale(pygame.image.load('image/burning_ship.png'), (240, 200))

        self.images = [self.triangle_de_sierpinski, self.mandelbrot, self.julia, self.flocon_de_koch, self.burning_ship]

        # Création des rectangles pour les images
        self.rect_triangle = pygame.Rect(0, 170, 240, 200)
        self.rect_mandelbrot = pygame.Rect(240, 170, 240, 200)
        self.rect_julia = pygame.Rect(480, 170, 240, 200)
        self.rect_flocon = pygame.Rect(720, 170, 240, 200)
        self.rect_burning_ship = pygame.Rect(960, 170, 240, 200)
    
    def display_image(self):
        # Fonction pour afficher les images
        x = 0
        y = 170
        for i in self.images:
            self.screen.blit(i, (x, y))
            x += 240
    
    def main_pygame(self): 
        # Boucle principale de Pygame
        while self.running: 
            self.display_image()
            for event in pygame.event.get():
                # Gestion de la fermeture de la fenêtre
                if event.type == pygame.QUIT:
                    self.running = False
                # Gestion des clics de souris sur les images pour ouvrir les fractales
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_triangle.collidepoint(event.pos):
                        self.sierpinski_script.show()
                    elif self.rect_mandelbrot.collidepoint(event.pos):
                        self.mandelbrot_script.show()
                    elif self.rect_julia.collidepoint(event.pos):
                        self.julia_script.show()
                    elif self.rect_flocon.collidepoint(event.pos):
                        print("yes")
                    elif self.rect_burning_ship.collidepoint(event.pos):
                        print("yes")
            
            pygame.display.flip()

if __name__ == "__main__":
    main = Main()
    main.main_pygame()
