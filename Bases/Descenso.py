"""This program can calc the descend gradient"""
import numpy as np

import matplotlib.pyplot as plt

function = lambda vp: np.sin(1 / 2 * vp[0] ** 2 - 1 / 4 * vp[1] ** 2 + 3) * np.cos(2 * vp[0] + 1 - np.e ** vp[1])

res = 100

_x = np.linspace(-2, 2, res)
_y = np.linspace(-2, 2, res)

_z = np.zeros((res, res))

for ix, x in enumerate(_x):
    for iy, y in enumerate(_y):
        _z[iy, ix] = function([x, y])

plt.contourf(_x, _y, _z, res)
plt.colorbar()

zeta = np.random.rand(2) * 4 - 2

_t = np.copy(zeta)

h = 0.001
lr = 0.003

plt.plot(zeta[0], zeta[1], "o", c="white")

grad = np.zeros(2)

for _ in range(10000):
    for it, vp in enumerate(zeta):
        _t = np.copy(zeta)

        _t[it] = _t[it] + h

        dv = (function(_t) - function(zeta)) / h

        grad[it] = dv

    zeta = zeta - lr * grad

    if _ % 50 == 0:
        plt.plot(zeta[0], zeta[1], ".", c="red")

plt.plot(zeta[0], zeta[1], "o", c="green")

plt.show()
