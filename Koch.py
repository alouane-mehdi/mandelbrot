import numpy as np
import matplotlib.pyplot as plt

def koch_snowflake(order, scale=10):
    def koch_curve(order):
        if order == 0:
            return np.array([[0, 0], [1, 0]])
        else:
            p1 = koch_curve(order-1)
            p2 = np.roll(p1, shift=-1, axis=0)
            angle = np.pi / 3
            rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            
            new_points = []
            for a, b in zip(p1, p2):
                new_points.append(a)
                new_points.append(a + (b-a)/3)
                new_points.append(a + (b-a)/3 + (rotation_matrix @ (b-a)/3))
                new_points.append(a + 2*(b-a)/3)
            new_points.append(p1[-1])
            return np.array(new_points)
    
    p = koch_curve(order)
    p = np.vstack([p, np.roll(p, shift=len(p)//3, axis=0)])
    p = np.vstack([p, np.roll(p, shift=2*len(p)//3, axis=0)])
    p *= scale
    
    return p

# Paramètres
order = 4
scale = 10

# Générer le flocon de Koch
snowflake = koch_snowflake(order, scale)

# Afficher le flocon de Koch
plt.figure(figsize=(8, 8))
plt.plot(snowflake[:, 0], snowflake[:, 1], 'b-')
plt.axis('equal')
plt.title(f'Flocon de Koch (ordre {order})')
plt.show()
