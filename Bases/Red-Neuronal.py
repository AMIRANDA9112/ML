import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

n  = 500
p = 2

X, Y = make_circles(n_samples=n, factor=0.5, noise=0.09)

Y = Y[:, np.newaxis]

plt.scatter(X[:, 0], X[:, 1])