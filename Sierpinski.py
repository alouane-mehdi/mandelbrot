import numpy as np
import matplotlib.pyplot as plt

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
