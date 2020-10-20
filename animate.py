import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import os

# Read matrixes generated at each iteration


def readOutputs(iteration):
    return np.loadtxt(f"outputs/{iteration + 1}"+'.txt')

# Create each frame


def createFrame(iteration):
    axis.imshow(animationData[iteration], cmap='hot_r', interpolation='nearest',
                vmin=0, vmax=100, extent=[0, 3, 0, 3])


# Saving init timestamp
start_time = time.time()

# Def consts and variables
OUTPUTS_FOLDER = 'outputs'
totalOutputs = 0,
animationData = []

# Getting number of iterations and animations seconds
for base, dirs, files in os.walk(OUTPUTS_FOLDER):
    for Files in files:
        totalOutputs += 1

numberOfSeconds = int(input("The number of outputs is " + str(totalOutputs) +
                            ", please enter the desired number of seconds:\n"))

# Saving all data needed to create animation
for i in range(totalOutputs):
    animationData.append(readOutputs(i))


# Matplotlib animation configs
fig, axis = plt.subplots()

axis.set(title="Distribuição de temperatura ao longo do tempo",
         xlabel="X", ylabel="Y")

axisImg = axis.imshow(animationData[0], cmap='hot_r', interpolation='nearest', vmin=0, vmax=100,
                      extent=[0, 3, 0, 3])
fig.colorbar(axisImg, label="Temperatura (K)")

# Creating and saving animation
animatedVideo = FuncAnimation(fig, createFrame, frames=totalOutputs)
animatedVideo.save("animation.mp4", fps=(totalOutputs/numberOfSeconds))

# Execution time
end_time = time.time()
print("Execution time (minutes):", round(end_time - start_time, 5))
