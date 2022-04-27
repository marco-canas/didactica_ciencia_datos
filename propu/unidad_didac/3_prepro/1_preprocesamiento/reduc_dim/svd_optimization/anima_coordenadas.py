import numpy as np
import matplotlib.pyplot as plt

#### datos
def datos(n):
    np.random.seed(42)
    xs = np.random.randn(n)
    ys = (1/4) * np.random.randn(n)
    D = np.c_[xs, ys]
    R45 = np.array([[np.cos(-np.pi/4), -np.sin(-np.pi/4)],
                    [np.sin(-np.pi/4),  np.cos(-np.pi/4)]])
    D_rotated = np.dot(D, R45)
    return D_rotated

Data = datos(20)

### recta inducida por un vector unitario

def unitario(theta):
    return np.array([np.cos(theta), np.sin(theta)]).reshape(-1, 1)

def dibuja_recta(theta):
    extremos = np.c_[2*unitario(theta), -2*unitario(theta)]
    plt.plot(extremos[0], extremos[1])

def matriz_proy(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c ** 2, c * s],
                     [c * s, s ** 2]])

def dibuja_perpendiculares(Data, theta):
    Data_p = np.dot(Data, matriz_proy(theta))
    for i in range(len(Data)):



        segmento = np.vstack([Data[i], Data_p[i]])
        plt.plot(segmento[:, 0], segmento[:, 1], 'b--')


theta = np.pi/24
dibuja_recta(theta)
plt.plot(Data[:, 0], Data[:, 1], 'o')
Data_p = np.dot(Data, matriz_proy(theta))
plt.plot(Data_p[:, 0], Data_p[:, 1], 'ro')
plt.axis('equal')
dibuja_perpendiculares(Data, theta)
plt.show()
