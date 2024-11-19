import numpy as np
import matplotlib.pyplot as plt

def eyler(a, b, h, f):

    x_1 = a
    y_1 = 1

    x_array = []
    y_array = []
    df_array = []

    y_old = y_1

    while x_1 < b:

        x_array.append(x_1)
        y_array.append(y_1)

        y_1 = y_1 + (h * f(x_1, y_1))
        
        df = (y_1 - y_old) / h
        df_array.append(df)

        y_old = y_1

        x_1 += h

    print("Останнє значення похідної =", df)

    plt.plot(x_array, y_array, color="b", label="Рішення для y(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()

    # plt.figure()
    # plt.plot(x_array, df_array, color="r", label="Похідна")
    # plt.xlabel("X")
    # plt.ylabel("dy/dx")
    # plt.grid(True)
    # plt.legend()

    plt.show()
