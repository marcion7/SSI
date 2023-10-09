import pandas as pd

class wczytaj_baze_probek_z_tekstem:
    def __init__(self, nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
        self.nazwa_pliku_z_wartosciami = nazwa_pliku_z_wartosciami
        self.nazwa_pliku_z_opisem_atr = nazwa_pliku_z_opisem_atr
        
    def probki(self):
        try:
            probki = pd.read_csv(self.nazwa_pliku_z_wartosciami, sep="\s+", header=None)
            probki = probki.T
            return probki
        except:
            print("Każda pojedyncza linia (próbka) musi zawierać taką samą liczbę wyrazów (wartości kolejnych atrybutów, deskryptorów)")
    
    def nazwy_atr(self):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        return atr[0]
    
    def czy_atr_symb(self, wiersz):
        atr = pd.read_csv(self.nazwa_pliku_z_opisem_atr, sep="\s+", header=None)
        if atr[1][wiersz] == 's':
            return True
        else:
            return False

test = wczytaj_baze_probek_z_tekstem("war.txt", "atr.txt")
print(test.probki()[0][2])
print(test.czy_atr_symb(4))
print(test.nazwy_atr()[4])