import math
import copy


# Calculating temperature in node at instant t
def newNodeTemperature(mesh, posX, posY, fourrier0):
    node_temperature = fourrier0*(
        mesh[posX + 1][posY] + mesh[posX - 1][posY] + mesh[posX][posY + 1] + mesh[posX][posY - 1])+(1 - 4*fourrier0)*mesh[posX][posY]
    return node_temperature

# Updating mesh temperatures


def updateMeshTemperatures(mesh, nodes, fourrier0):
    auxmesh = copy.deepcopy(mesh)
    max_variation = 0
    for i in range(nodes):
        for j in range(nodes):
            if 0 < i < (1 + 2*(nodes/3)) and 0 < j < (nodes/3) - 1 or (2*(nodes/3)) < i < nodes - 1 and 0 < j < nodes - 1:
                auxmesh[i][j] = round(
                    newNodeTemperature(mesh, i, j, fourrier0), 3)
                if abs(auxmesh[i][j] - mesh[i][j]) > max_variation and (auxmesh[i][j] - mesh[i][j]) != 0:
                    max_variation = abs(auxmesh[i][j] - mesh[i][j])
    return auxmesh, max_variation
