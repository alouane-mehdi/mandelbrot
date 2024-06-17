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
        
class BurningShip:
    def __init__(self) -> None:
        self.width, self.height = 800, 800
        self.x_min, self.x_max = -2.5, 1.5
        self.y_min, self.y_max = -2, 2
        self.max_iter = 256

        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        self.C = X + 1j * Y

        self.Z = np.zeros_like(self.C)
        self.img = np.zeros(self.C.shape, dtype=int)
    
    def compute(self):
        for i in range(self.max_iter):
            mask = abs(self.Z) < 2
            self.img[mask] = i
            self.Z[mask] = (np.abs(self.Z[mask].real) + 1j * np.abs(self.Z[mask].imag))**2 + self.C[mask]

    def display(self):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')
        plt.colorbar()
        plt.title("Fractale de Burning Ship")
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
        


class FloconDeKoch:
    def __init__(self, iterations):
        # Nombre d'itérations pour la construction du flocon
        self.iterations = iterations

    def courbe_de_koch(self, p1, p2, iterations):
        if iterations == 0:
            return [p1, p2]
        
        # Calcul des points intermédiaires entre p1 et p2
        p1 = np.array(p1)
        p2 = np.array(p2)
        s = (2 * p1 + p2) / 3
        t = (p1 + 2 * p2) / 3
        u = s + np.dot([[np.cos(np.pi/3), -np.sin(np.pi/3)], [np.sin(np.pi/3), np.cos(np.pi/3)]], (t - s))
        
        # Application récursive du processus de la courbe de Koch
        return (self.courbe_de_koch(p1, s, iterations - 1) +
                self.courbe_de_koch(s, u, iterations - 1)[1:] +
                self.courbe_de_koch(u, t, iterations - 1)[1:] +
                self.courbe_de_koch(t, p2, iterations - 1)[1:])
    
    def generer(self):
        # Triangle équilatéral initial
        p1 = [0, 0]
        p2 = [1, 0]
        p3 = [0.5, np.sin(np.pi/3)]
        
        # Génération de la courbe de Koch pour chaque côté du triangle
        cote1 = self.courbe_de_koch(p1, p2, self.iterations)
        cote2 = self.courbe_de_koch(p2, p3, self.iterations)
        cote3 = self.courbe_de_koch(p3, p1, self.iterations)
        
        # Combinaison des points
        self.points = cote1[:-1] + cote2[:-1] + cote3
    
    def afficher(self):
        self.generer()
        # Extraction des coordonnées x et y
        x, y = zip(*self.points)
        
        plt.figure(figsize=(10, 10))
        plt.plot(x, y, 'b-')
        plt.title("Flocon de Koch avec {} itérations".format(self.iterations))
        plt.axis('equal')
        plt.show()
    
    def show(self):
        self.afficher()
        
        
class Sierpinski:
    def __init__(self) -> None:
        
        # Dimensions du plot
        self.width, self.height = 800, 800

        # Nombre d'itérations
        self.max_iter = 10000

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
                
        