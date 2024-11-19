import numpy as np
import matplotlib.pyplot as plt

def runge(a, b, h, f):
    x = a
    y = 1

    x_arr = [x]
    y_arr = [y]

    while x < b:
        k1 = f(x, y)
        k2 = f(x + (h/2), y + (h/2)*k1)
        k3 = f(x + (h/2), y + (h/2)*k2)
        k4 = f(x + h, y + h*k3)
        y = y + (h/6)*(k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        x_arr.append(x)
        y_arr.append(y)

    plt.plot(x_arr, y_arr, color="b")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()