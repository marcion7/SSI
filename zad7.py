import numpy as np

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
                self.weights_table[i][j] += wyjscie[0][i] * wyjscie[0][j]
            self.weights_table[i] /= self.n
        return self.weights_table
    
    def rozpoznaj_obraz(self, obraz):
        wyjscie = obraz.reshape(1, len(obraz[0]) * len(obraz[1]))
        for i in range(self.n):
            suma = 0
            for j in range(self.n):
                if i == j:
                    continue
                suma += wyjscie[0][j] * self.weights_table[i][j]
            wyjscie[0][i] = 1 if suma >= 0 else -1
        if np.array_equal(wyjscie, obraz):
            return False
        return obraz
    
hopfield = Siec_hopfielda(5,5)
for wzor in baza_wzor:
    hopfield.naucz_obraz(wzor)
print(hopfield.rozpoznaj_obraz(baza_test[1]))

