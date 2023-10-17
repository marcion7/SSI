import numpy as np
import matplotlib.pyplot as plt
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
    return V

colors = ['r', 'b', 'g', 'y']

test = WczytajBazeProbekZTekstem("spirala.txt", "spirala-type.txt")
print(KMeans(test.Probki(), 3, 4))



