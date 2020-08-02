# The paramater determines whether the graph is going to be of the quadratic function (2)
# cubic function (3), quartic function (4) etc.

from matplotlib import pyplot as plt
import numpy as np


def poly_func(degree):
    try:
        x = np.arange(-15, 16)
        y = x ** degree

        plt.plot(x, y)
        plt.grid()
        plt.show()

    except ValueError:
        print("Value to low, enter a greater number")


poly_func(-1)


