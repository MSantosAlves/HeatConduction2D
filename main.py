from build_mesh import createMesh
from numeric_solution import updateMeshTemperatures
from plot import plotHeatMap
from saveMatrixes import saveMatrix
from profiles import plotTemperatureProfile
import time

start_time = time.time()
# Defining constants and variables
max_variation = 1000
TOLERANCE = 0.1
iteration = 1
positionY = 0

# Getting mesh, Fourrier constant and number of cells on each direction
mesh, FOURRIER_NUMBER, nodes = createMesh()

nb_plots = int(
    input("Please enter the desired number of temperature profiles:\n"))
plotPass = round(3/nb_plots, 1)


# Iterating mesh using contour conditions
while max_variation > TOLERANCE:
    mesh, max_variation = updateMeshTemperatures(mesh, nodes, FOURRIER_NUMBER)
    if max_variation > 0.1:
        saveMatrix(mesh, nodes, iteration)
    print("Max. temperature variation:", max_variation)
    iteration = iteration + 1

# Creating temperature profiles
while positionY < 3:
    plotTemperatureProfile(mesh, positionY, nodes)
    positionY = round((plotPass + positionY), 1)

end_time = time.time()
print("Execution time (minutes):", round(end_time - start_time, 5))
# Ploting final mesh
plotHeatMap(mesh, nodes, iteration)
