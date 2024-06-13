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