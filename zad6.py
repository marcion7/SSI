import numpy as np
import matplotlib.pyplot as plt

def euc_distance2d(p1, p2):
    return np.sqrt(pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2))

baza_wzor = [
    np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]),
    np.array([[1, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 0]]),
]

baza_test = [
    np.array([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]]),
]

def miara_nieprawdopodobienstwa(BA, BB):
    miara = 0
    for pay in range(len(BA)):
        for pax in range(len(BA[pay])):
            if BA[pay, pax] == 1:
                odl_min = np.inf
                for pby in range(len(BB)):
                    for pbx in range(len(BB[pby])):
                        if BB[pby, pbx] == 1:
                            odl_akt = euc_distance2d((pay, pax),(pby, pbx))
                            odl_min = min(odl_min, odl_akt)
                miara += odl_min
    return miara

def miara_podobienstwa_obustronnego(BA, BB):
    wynik = miara_nieprawdopodobienstwa(BA, BB) + miara_nieprawdopodobienstwa(BB, BA)
    return -wynik

def zachlanne_dopasowanie(bitmap_test, bitmap_wzor):
    miara = -np.inf
    index = 0
    for i in range(len(bitmap_wzor)):
        miara_podob_obustronnego = miara_podobienstwa_obustronnego(bitmap_test, bitmap_wzor[i])
        if miara_podob_obustronnego > miara:
            miara = miara_podob_obustronnego
            index = i
    return bitmap_test, baza_wzor[index]

for i in range(len(baza_test)):
    bitmap_test, bitmap_wzor = zachlanne_dopasowanie(baza_test[i], baza_wzor)
    print(f'Dla bitmapy testowej {i+1}:\n{bitmap_test}\nNajbardziej podobna jest bitmapa wzorcowa:\n{bitmap_wzor}')
    plt.subplot(1, 2, 1)
    plt.imshow(bitmap_test, interpolation='nearest', cmap='Greys')
    plt.title(f'Bitmapa testowa {i+1}')
    plt.subplot(1, 2, 2)
    plt.imshow(bitmap_wzor, interpolation='nearest', cmap='Greys')
    plt.title(f'Najbardziej podobny wzór')
    plt.show()
