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

test = WczytajBazeProbekZTekstem("iris.txt", "atr.txt")

def SplitData(data):
    class_label = data.iloc[:, -1]
    classes = np.unique(class_label)
    series_dict = {}
    for c in classes:
        series_dict[c] = data[data.iloc[:, -1] == c].iloc[:, :-1]
    return series_dict

data_splited = SplitData(test.Probki())

plt.figure(figsize=(12, 8))

# 1
plt.subplot(2, 2, 1)
for class_label, data in data_splited.items():
    plt.scatter(data[2], data[3], label=f'Class {class_label}')
plt.xlabel('Atrybut 3')
plt.ylabel('Atrybut 4')
plt.legend()

# 2
plt.subplot(2, 2, 2)
for class_label, data in data_splited.items():
    plt.scatter(data[1], data[3], label=f'Class {class_label}')
plt.xlabel('Atrybut 2')
plt.ylabel('Atrybut 4')
plt.legend()

# 3
plt.subplot(2, 2, 3)
for class_label, data in data_splited.items():
    plt.scatter(data[0], data[3], label=f'Class {class_label}')
plt.xlabel('Atrybut 1')
plt.ylabel('Atrybut 4')
plt.legend()

# 4
plt.subplot(2, 2, 4)
for class_label, data in data_splited.items():
    plt.scatter(data[1], data[2], label=f'Class {class_label}')
plt.xlabel('Atrybut 2')
plt.ylabel('Atrybut 3')
plt.legend()

plt.show()
