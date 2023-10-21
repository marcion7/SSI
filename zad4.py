import numpy as np
import matplotlib.pyplot as plt

def funkcja_przystosowania(x):
    return np.sin(x/10)*np.sin(x/200)

def algorithm_1plus1(rozrzut, wsp_przyrostu, l_iteracji, zakres_zmiennosci = [0, 100]):
    x = np.random.uniform(zakres_zmiennosci[0], zakres_zmiennosci[1])
    y = funkcja_przystosowania(x)
    for i in range(l_iteracji):
        x_pot = x + np.random.uniform(-rozrzut, rozrzut)
        if x_pot > zakres_zmiennosci[1]:
            x_pot = zakres_zmiennosci[1]
        elif x_pot < zakres_zmiennosci[0]:
            x_pot = zakres_zmiennosci
        y_pot = funkcja_przystosowania(x_pot)

        if y_pot >= y:
            x = x_pot
            y = y_pot
        else:
            rozrzut /= wsp_przyrostu
        print(f"Iteracja nr: {i+1}")
        print(f"x = {x}, y = {y}, rozrzut = {rozrzut}")
        print('-----------------------------------------------------------------------')
        plt.scatter(x, y)
    x = np.arange(0, 100)
    plt.title('Algorytm 1+1')
    plt.plot(x, funkcja_przystosowania(x), label='f(x)=sin(x/10)*sin(x/200)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

algorithm_1plus1(10, 1.1, 100)
