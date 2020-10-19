import numpy as np

# Defining constants and variables
ALPHA = 1

# Building the mesh with L profile


def createMesh():
    nodes = int(input("Please enter the number n of nxn matrix:\n"))

    DELTA_X = 3/nodes
    delta_time = pow((3/nodes), 2)*0.1
    FOURRIER_0 = ((ALPHA*delta_time)/pow(DELTA_X, 2))

    mesh = []

    for i in range(nodes):
        row = []
        for j in range(nodes):
            if j >= nodes/3 and i < (nodes/3)*2:
                row.append(None)
            else:
                row.append(0)
        mesh.append(row)

# Creating the contour conditions
    for i in range(nodes):
        row = mesh[i]
        for j in range(nodes):
            if i == 0 and row[j] is not None:
                row[j] = 100
            elif i == nodes - 1:
                row[j] = 100
            elif j == 0 and 0 < i < (nodes - 1):
                row[j] = 100
            elif j == nodes - 1 and (nodes/3)*2 < i < nodes - 1:
                row[j] = 30
            elif j == nodes/3 - 1 and i < (nodes/3)*2:
                row[j] = 40
            elif i == (nodes/3)*2 and j >= (nodes/3) - 1:
                row[j] = 20
        mesh[i] = row
    return mesh, FOURRIER_0, nodes
