import numpy as np


def fixMesh(mesh, nodes):
    for i in range(nodes):
        for j in range(nodes):
            if mesh[i][j] == None:
                mesh[i][j] = 0
    return mesh


def saveMatrix(mesh, nodes, iteration):
    np.savetxt(f'outputs/'+str(iteration)+'.txt', fixMesh(mesh, nodes))
