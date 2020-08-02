from matplotlib import pyplot as plt
import numpy as np
from math import pi

print("What type of graph do you want?: ")
print("\n")
trig_type = input("SIN for sine, COS for cosine and TAN for tangent: ")

x, y = [], []

if trig_type.lower() == "sin":
    x = np.linspace(0, 2 * pi, 360)
    y = np.sin(x)

elif trig_type.lower() == "cos":
    x = np.linspace(0, 2 * pi, 360)
    y = np.cos(x)


elif trig_type.lower() == "tan":
    x = np.linspace(0, 2 * pi, 180)
    y = np.tan(x)

plt.plot(x, y)
plt.grid()
plt.show()

