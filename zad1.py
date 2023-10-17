import pandas as pd


class WczytajBazeProbekZTekstem:
    def __init__(self, nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
        self.nazwa_pliku_z_wartosciami = nazwa_pliku_z_wartosciami
        self.nazwa_pliku_z_opisem_atr = nazwa_pliku_z_opisem_atr

    def NazwyAtr(self):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        return list(atr[0])

    def Probki(self):
            names = self.NazwyAtr()
            probki = pd.read_csv(self.nazwa_pliku_z_wartosciami, sep="\s+", names=names)
            return probki

    def CzyAtrSymb(self, wiersz):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        if atr[1][wiersz] == 's':
            return True
        else:
            return False


test = WczytajBazeProbekZTekstem("spirala.txt", "spirala-type.txt")
# print(test.Probki())
# print(test.CzyAtrSymb(0))
# print(test.NazwyAtr()[0])
