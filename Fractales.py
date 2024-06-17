import numpy as np
import matplotlib.pyplot as plt

class Julia:
    def __init__(self) -> None:
        
        #width and height init
        self.width, self.height = 800, 800

        # real and imaginary abscissa and ordinate 
        self.x_min, self.x_max = -2, 2
        self.y_min, self.y_max = -2, 2

        # Constante complexe c
        self.c = complex(-0.7, 0.27)

        # iteration maximum 
        self.max_iter = 256

        # create de grid of complex point
        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        self.Z = X + 1j * Y

        # array to stock the results
        self.img = np.zeros(self.Z.shape, dtype=int)
    
    def compute(self):
        # Calculation of the Julia set
        for i in range(self.max_iter):
            mask = abs(self.Z) < 2
            self.img[mask] = i
            self.Z[mask] = self.Z[mask]**2 + self.c

    def display(self):
        # display with matplotlib
        plt.figure(figsize=(10, 10))
        plt.imshow(self.img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')
        plt.colorbar()
        plt.title("Ensemble de Julia pour c = {}".format(self.c))
        plt.xlabel("Partie Réelle")
        plt.ylabel("Partie Imaginaire")
        plt.show()
    
    def show(self):
        self.compute()
        self.display()

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

class Sierpinski:
    def __init__(self) -> None:
        
        # Dimensions du plot
        self.width, self.height = 800, 800

        # Nombre d'itérations
        self.max_iter = 8

        # Initialisation des points
        self.points = np.zeros((self.max_iter, 2))

        # Sommets du triangle
        self.vertices = np.array([[0, 0], [2, 0], [1, np.sqrt(3)]])
    
    def compute(self):
        # Point initial au centre du triangle
        self.points[0] = [1, np.sqrt(3) / 3]
        
        for i in range(1, self.max_iter):
            vertex = self.vertices[np.random.randint(0, 3)]
            self.points[i] = (self.points[i - 1] + vertex) / 2

    def display(self):
        # Affichage avec matplotlib
        plt.figure(figsize=(10, 10))
        plt.scatter(self.points[:, 0], self.points[:, 1], s=0.1, color='black')
        plt.title("Triangle de Sierpinski")
        plt.axis('equal')
        plt.axis('off')
        plt.show()
    
    def show(self):
        self.compute()
        self.display()
