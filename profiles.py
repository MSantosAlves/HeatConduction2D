import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting time x n graphic
with open('timeXn.txt') as f:
    lines = f.readlines()
    t = [line.split()[0] for line in lines]
    n = [line.split()[1] for line in lines]

fig, ax = plt.subplots()
ax.plot(t, n)

ax.set(xlabel='Número de nós (n)', ylabel='Tempo de execução (s)',
       title='Tempo computacional')
ax.grid()

fig.savefig("timeXn.png")


def plotTemperatureProfile(mesh, posY, nodes):
    if posY != 0:
        matrixLine = int((nodes/3)*(3 - posY))
    else:
        matrixLine = nodes - 1
    temperatures = mesh[matrixLine]
    nonZeroTemperatures = []
    for i in range(nodes):
        if temperatures[i] is not None:
            nonZeroTemperatures.append(temperatures[i])
    xSize = len(nonZeroTemperatures)
    xAxis = []
    for i in range(xSize):
        xAxis.append(i)

    fig, ax = plt.subplots()
    ax.plot(xAxis, nonZeroTemperatures)

    ax.set(xlabel='Posição no eixo x (em relação aos nós)', ylabel='Temperatura (K)',
           title='Perfil de temperatura para y = ' + str(posY) + "m")
    ax.grid()

    fig.savefig("profiles/profile" + str(posY) + ".png")
