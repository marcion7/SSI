import matplotlib.pyplot as plt
import numpy as np
from zad1 import WczytajBazeProbekZTekstem

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
plt.show()

test = WczytajBazeProbekZTekstem("iris.txt", "iris-type.txt")

def SplitData(data):
    class_label = data.iloc[:, -1]
    classes = np.unique(class_label)
    series_dict = {}
    for c in classes:
        series_dict[c] = data[data.iloc[:, -1] == c].iloc[:, :-1]
    return series_dict

data_splited = SplitData(test.Probki())
atr = test.NazwyAtr()

def SetClasess(str):
    classes = str.split('(')[1]
    classes = classes.split(')')[0]
    classes= dict(i.split('=') for i in classes.split(','))
    return classes

classes = SetClasess(atr[4])

plt.figure(figsize=(12, 8))
plt.suptitle("Punkty dla klasy Irys")

# 1
plt.subplot(2, 2, 1)
for class_label, data in data_splited.items():
    plt.scatter(data.iloc[:, 2], data.iloc[:, 3], label=classes[str(class_label)])
plt.xlabel(atr[2])
plt.ylabel(atr[3])
plt.legend()

# 2
plt.subplot(2, 2, 2)
for class_label, data in data_splited.items():
    plt.scatter(data.iloc[:, 1], data.iloc[:, 3], label=classes[str(class_label)])
plt.xlabel(atr[1])
plt.ylabel(atr[3])
plt.legend()

# 3
plt.subplot(2, 2, 3)
for class_label, data in data_splited.items():
    plt.scatter(data.iloc[:, 0], data.iloc[:, 3], label=classes[str(class_label)])
plt.xlabel(atr[0])
plt.ylabel(atr[3])
plt.legend()

# 4
plt.subplot(2, 2, 4)
for class_label, data in data_splited.items():
    plt.scatter(data.iloc[:, 1], data.iloc[:, 2], label=classes[str(class_label)])
plt.xlabel(atr[1])
plt.ylabel(atr[2])
plt.legend()

plt.show()
