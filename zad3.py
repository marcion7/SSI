import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from zad1 import WczytajBazeProbekZTekstem

def EucDist(p1, p2):
    return np.sqrt(pow(p2.x-p1.x, 2)+pow(p2.y-p1.y, 2))

def KMeans(data, iters, n):
    V = data.sample(n)
    V = V.reset_index()
    data['Us'] = None
    for _ in range(iters):
        for s in range(len(data.index)):
            distance = np.inf
            for j in range(len(V.index)):
                if EucDist(V.iloc[j], data.iloc[s]) < distance:
                    distance = EucDist(V.iloc[j], data.iloc[s])
                    data.at[s, 'Us'] = j

        for i in range(len(V.index)):
            Xgr = data.loc[data['Us'] == i]
            if Xgr.size == 0:
                break
            else:
                V.loc[i, 'x'] = Xgr['x'].mean()
                V.loc[i, 'y'] = Xgr['y'].mean()
    plt.title(f'Algorytm k-średnich\nLiczba iteracji: {iters}')
    KMeans_plot(V, data)

def KMeans_plot(V, data):
    color = cm.viridis_r(np.linspace(0, 1, len(V.index)))
    for n in range(len(V.index)):
        part = data.loc[data['Us'] == n]
        plt.scatter(
            part['x'],
            part['y'],
            color=color[n])
        plt.scatter(
            V.loc[n, 'x'],
            V.loc[n, 'y'],
            color=color[n],
            marker='^',
            edgecolors='#000000',
            label=f"group {n}")
    plt.xlabel('atrybut 1')
    plt.ylabel('atrybut 2')
    plt.legend(loc="upper right")
    plt.show()


test = WczytajBazeProbekZTekstem("spirala.txt", "spirala-type.txt")
KMeans(test.Probki(), 11, 4)
