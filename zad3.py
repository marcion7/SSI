import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from zad1 import WczytajBazeProbekZTekstem

def EucDist(p1, p2):
    return np.sqrt(pow(p2.x-p1.x, 2)+pow(p2.y-p1.y, 2))

def KMeans(data, n, iters):
    V = data.sample(n)
    V = V.reset_index()
    data['Us'] = None
    for _ in range(iters):
        for s in range(len(data.index)):
            distance = np.inf
            for x in range(len(V.index)):
                if distance > EucDist(V.iloc[x], data.iloc[s]):
                    distance = EucDist(V.iloc[x], data.iloc[s])
                    data.at[s, 'Us'] = x

        for j in range(len(V.index)):
            Xgr = data.loc[data['Us'] == j]
            if Xgr is None:
                continue
            else:
                V.loc[j, 'x'] = Xgr['x'].mean()
                V.loc[j, 'y'] = Xgr['y'].mean()
        
    plt.title(f'Algorytm k-średnich \n Liczba iteracji: {iters}')
    kMeansPlot(V, data)

def kMeansPlot(V, data):
    color = cm.viridis_r(np.linspace(0, 1, len(V.index)))
    for n in range(len(V.index)):
        part = data.loc[data['Us'] == n]
        plt.scatter(
            part['x'],
            part['y'],
            c=color[n]
        )
        plt.scatter(
            V.loc[n, 'x'],
            V.loc[n, 'y'],
            c=color[n],
            marker='s',
            edgecolors='#000000',
            label=(f"group {n}")
        )
    plt.xlabel('atrybut 1')
    plt.ylabel('atrybut 2')
    plt.legend()
    plt.show()

test = WczytajBazeProbekZTekstem("spirala.txt", "spirala-type.txt")
KMeans(test.Probki(), 4, 11)
