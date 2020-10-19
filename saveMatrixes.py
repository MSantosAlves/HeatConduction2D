import numpy as np


def fixMesh(mesh, nodes):
    for i in range(nodes):
        for j in range(nodes):
            if mesh[i][j] == None:
                mesh[i][j] = 0
    return mesh


def saveMatrix(mesh, nodes, iteration):
    with open('outputs/'+str(iteration)+'.txt', 'w') as file:
        file.write(str(np.matrix(fixMesh(mesh, nodes))))
