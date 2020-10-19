import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def fixMesh(mesh, nodes):
    for i in range(nodes):
        for j in range(nodes):
            if mesh[i][j] == None:
                mesh[i][j] = 0
    return mesh


def plotHeatMap(mesh, nodes, iteration):
    finalMeshe = fixMesh(mesh, nodes)
    plt.imshow(finalMeshe, cmap='hot_r', interpolation='nearest',
               vmin=0, vmax=100, extent=[0, 3, 0, 3])
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.suptitle(
        "Geometria 2D em formato de L")
    plt.title(f'Número de nós: {nodes ** 2}')
    plt.colorbar(label="Temperatura (K)")
    plt.savefig('finalPlot.png')
