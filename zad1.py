import pandas as pd

class WczytajBazeProbekZTekstem:
    def __init__(self, nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
        self.nazwa_pliku_z_wartosciami = nazwa_pliku_z_wartosciami
        self.nazwa_pliku_z_opisem_atr = nazwa_pliku_z_opisem_atr
        
    def Probki(self):
        try:
            probki = pd.read_csv(self.nazwa_pliku_z_wartosciami, sep="\s+", header=None)
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

test = WczytajBazeProbekZTekstem("war.txt", "atr.txt")
print(test.Probki()[0][2])
print(test.CzyAtrSymb(4))
print(test.NazwyAtr()[4])
