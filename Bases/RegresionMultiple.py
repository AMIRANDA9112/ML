import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

boston = load_boston()



X = (boston.data).T
Y = np.array(boston.target)
print(X)
plt.scatter(X, Y, alpha=0.3)

X = np.array([np.ones(506), X]).T
"""creamos una matrix con el array X y le sumamos una array de 1 """
B = np.linalg.inv(X.T @ X) @ X.T @ Y
"""formula para minimizar el error cuadratico medio"""
plt.plot([4, 9], [B[0] + B[1] * 4, B[0] + B[1] * 9], c="red")
"""plot de linea roja de la funcion de coste calculada"""
plt.show()
