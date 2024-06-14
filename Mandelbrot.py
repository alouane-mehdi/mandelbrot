import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
    def __init__(self) -> None:
        
        # Dimensions du plot
        self.width, self.height = 800, 800

        # Limites de l'axe complexe
        self.x_min, self.x_max = -2.5, 1.5
        self.y_min, self.y_max = -2, 2

        # Nombre d'itérations maximum
        self.max_iter = 256

        # Création de la grille de points complexes
        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        self.C = X + 1j * Y

        # Initialisation des tableaux Z et img
        self.Z = np.zeros_like(self.C)
        self.img = np.zeros(self.C.shape, dtype=int)
    
    def compute(self):
        # Calcul de l'ensemble de Mandelbrot
        for i in range(self.max_iter):
            mask = abs(self.Z) < 2
            self.img[mask] = i
            self.Z[mask] = self.Z[mask]**2 + self.C[mask]

    def display(self):
        # Affichage avec Matplotlib
        plt.figure(figsize=(10, 10))
        plt.imshow(self.img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')
        plt.colorbar()
        plt.title("Ensemble de Mandelbrot")
        plt.xlabel("Partie Réelle")
        plt.ylabel("Partie Imaginaire")
        plt.show()
    
    def show(self):
        self.compute()
        self.display()
