import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [-2, -1.8, -1.4, -0.7, 0, 0.7, 1.4, 1.8, 2, 1.8, 1.4, 0.8, 0, -0.8, -1.4, -1.8, -2]
y1 = [0, 0.8, 1.4, 1.9, 2, 1.9, 1.4, 0.8, 0, -0.8, -1.4, -1.9, -2, -1.9, -1.4, -0.8, 0]

x2 = [-1, 0, 1]
y2 = [1, 0, 1]

sin = np.linspace(np.pi, 2*np.pi, 200)
x3 = np.arange(-1, 1, 0.01)
y3 = np.sin(sin)

plt.plot(x1, y1, label='lamane', color='r')
plt.scatter(x2, y2, label='punkty', color='b', marker='D')
plt.plot(x3, y3, label='sinus', color='y')

plt.legend()
plt.ylim(-3,3)
plt.grid()
#plt.show()

class WczytajBazeProbekZTekstem:
    def __init__(self, nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
        self.nazwa_pliku_z_wartosciami = nazwa_pliku_z_wartosciami
        self.nazwa_pliku_z_opisem_atr = nazwa_pliku_z_opisem_atr
        
    def Probki(self):
        try:
            probki = pd.read_csv(self.nazwa_pliku_z_wartosciami, sep="\s+", header=None)
            probki = probki.T
            return probki
        except:
            print("Każda pojedyncza linia (próbka) musi zawierać taką samą liczbę wyrazów (wartości kolejnych atrybutów, deskryptorów)")
    
    def NazwyAtr(self):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        return atr[0]
    
    def CzyAtrSymb(self, wiersz):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        if atr[1][wiersz] == 's':
            return True
        else:
            return False

test = WczytajBazeProbekZTekstem("iris.txt", "atr.txt")
print(test.Probki()[0][2])

seria1 = []
for row in test.Probki:
    if test.Probki