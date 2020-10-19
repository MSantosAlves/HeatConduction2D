from build_mesh import createMesh
from numeric_solution import updateMeshTemperatures
from plot import plotHeatMap
from saveMatrixes import saveMatrix
import time


start_time = time.time()
# Defining constants and variables
max_variation = 1000
TOLERANCE = 1e-5
iteration = 1

# Getting mesh, Fourrier constant and number of cells on each direction
mesh, FOURRIER_NUMBER, nodes = createMesh()

# Iterating mesh using contour conditions
while max_variation > TOLERANCE:
    mesh, max_variation = updateMeshTemperatures(mesh, nodes, FOURRIER_NUMBER)
    if max_variation > 0.1:
        saveMatrix(mesh, nodes, iteration)
    print("Max. temperature variation:", max_variation)
    iteration = iteration + 1


end_time = time.time()
total_time = end_time - start_time
# Ploting final mesh
plotHeatMap(mesh, nodes, iteration)
print("Execution time (seconds):", round(total_time, 2))
# print("Press ctrl + c to exit programm.")
