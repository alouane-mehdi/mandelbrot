# BurningShip.py
import numpy as np
import matplotlib.pyplot as plt

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
