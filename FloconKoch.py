import matplotlib.pyplot as plt
import numpy as np

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

