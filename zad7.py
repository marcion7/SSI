import numpy as np
import matplotlib.pyplot as plt

baza_wzor = [
    np.array([[1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1]]),
    np.array([[1, -1, -1, -1, 1], [-1, 1, -1, 1, -1], [-1, -1, 1, -1, -1], [-1, 1, -1, 1, -1], [1, -1, -1, -1, 1]]),
    np.array([[-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1], [1, 1, 1, 1, 1], [-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1]]),
]

baza_test = [
    np.array([[-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1]]),
    np.array([[1, 1, -1, -1, 1], [-1, 1, -1, 1, -1], [-1, 1, 1, 1, -1], [-1, 1, -1, 1, -1], [1, 1, -1, -1, 1]]),
    np.array([[-1, -1, -1, -1, -1], [-1, -1, 1, -1, -1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1], [-1, -1, 1, -1, -1]]),
    np.array([[-1, 1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1]]),
]


class Siec_hopfielda:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.n = h * w
        self.weights_table = np.zeros((self.n, self.n))
    
    def naucz_obraz(self, wzor):
        wyjscie = wzor.reshape(1, len(wzor[0]) * len(wzor[1]))
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    continue
                self.weights_table[i][j] += (wyjscie[0][i] * wyjscie[0][j]) / self.n
    
    def rozpoznaj_obraz(self, obraz):
        wyjscie = obraz.reshape(1, len(obraz[0]) * len(obraz[1]))
        for i in range(self.n):
            suma = 0
            for j in range(self.n):
                if i == j:
                    continue
                suma += wyjscie[0][j] * self.weights_table[i][j]
            wyjscie[0][i] = 1 if suma >= 0 else -1
        obraz_skorygowany = wyjscie.reshape(len(obraz[0]), len(obraz[1]))
        obraz_negatyw = obraz
        for x in range(len(obraz[0])):
            for y in range(len(obraz[1])):
                obraz_negatyw[x, y] = 1 if obraz_negatyw[x, y] == -1 else -1
        if np.array_equal(obraz_skorygowany, obraz) or np.array_equal(obraz_skorygowany, obraz_negatyw):
            return obraz_skorygowany
        return self.rozpoznaj_obraz(obraz_skorygowany)
    
hopfield = Siec_hopfielda(5,5)
for wzor in baza_wzor:
    hopfield.naucz_obraz(wzor)

for i in range(len(baza_test)):
    plt.subplot(1, 2, 1)
    plt.imshow(baza_test[i], interpolation='nearest', cmap='Greys')
    plt.title(f'Znak testowy {i+1}')
    plt.subplot(1, 2, 2)
    plt.imshow(hopfield.rozpoznaj_obraz(baza_test[i]), interpolation='nearest', cmap='Greys')
    plt.title(f'Po korekcji')
    plt.show()
