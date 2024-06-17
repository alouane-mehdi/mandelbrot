import pygame
from fractales import FloconDeKoch, Sierpinski, Mandelbrot, BurningShip, Julia

class Main:
    def __init__(self):
        self.julia_script = Julia()
        self.sierpinski_script = Sierpinski()
        self.mandelbrot_script = Mandelbrot()
        self.burning_ship_script = BurningShip()
        self.koch_snowflake_script = FloconDeKoch(iterations=5)

        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((1200, 500))

        self.triangle_de_sierpinski = pygame.transform.scale(pygame.image.load('image/triangle_de_sierpinski.png'), (240, 200))
        self.mandelbrot = pygame.transform.scale(pygame.image.load('image/mandelbrot.jpeg'), (240, 200))
        self.julia = pygame.transform.scale(pygame.image.load('image/Julia.png'), (240, 200))
        self.flocon_de_koch = pygame.transform.scale(pygame.image.load('image/flocon_de_koch.jpeg'), (240, 200))
        self.burning_ship = pygame.transform.scale(pygame.image.load('image/burning_ship.png'), (240, 200))

        self.images = [self.triangle_de_sierpinski, self.mandelbrot, self.julia, self.flocon_de_koch, self.burning_ship]

        self.rect_triangle = pygame.Rect(0, 170, 240, 200)
        self.rect_mandelbrot = pygame.Rect(240, 170, 240, 200)
        self.rect_julia = pygame.Rect(480, 170, 240, 200)
        self.rect_flocon = pygame.Rect(720, 170, 240, 200)
        self.rect_burning_ship = pygame.Rect(960, 170, 240, 200)

    def display_image(self):
        x = 0
        y = 170
        for img in self.images:
            self.screen.blit(img, (x, y))
            x += 240

    def main_pygame(self):
        while self.running:
            self.screen.fill((255, 255, 255))  # Effacer l'écran avec une couleur de fond
            self.display_image()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_triangle.collidepoint(event.pos):
                        self.sierpinski_script.show()
                    elif self.rect_mandelbrot.collidepoint(event.pos):
                        self.mandelbrot_script.show()
                    elif self.rect_julia.collidepoint(event.pos):
                        self.julia_script.show()
                    elif self.rect_flocon.collidepoint(event.pos):
                        self.koch_snowflake_script.show()
                    elif self.rect_burning_ship.collidepoint(event.pos):
                        self.burning_ship_script.show()

            pygame.display.flip()

if __name__ == "__main__":
    main = Main()
    main.main_pygame()

