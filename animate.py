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
    axes.imshow(animationData[iteration], cmap='hot_r', interpolation='nearest',
                vmin=0, vmax=100, extent=[0, 3, 0, 3])


# Saving init timestamp
start_time = time.time()

# Def consts and variables
OUTPUTS_FOLDER = 'outputs'
totalOutputs = 0
animationData = []
numberOfSeconds = int(input("Please enter the desired number of seconds:\n"))

# Getting number of iterations
for base, dirs, files in os.walk(OUTPUTS_FOLDER):
    for Files in files:
        totalOutputs += 1

# Saving all data needed to create animation
for i in range(totalOutputs):
    animationData.append(readOutputs(i))


# Matplotlib animation configs
fig, axes = plt.subplots()

axes.set(title="Distribuição de temperatura ao longo do tempo",
         xlabel="X", ylabel="Y")

axesImg = axes.imshow(animationData[0], cmap='hot_r', interpolation='nearest', vmin=0, vmax=100,
                      extent=[0, 3, 0, 3])
fig.colorbar(axesImg, label="Temperatura (K)")

# Creating and saving animation
animatedVideo = FuncAnimation(fig, createFrame, frames=totalOutputs)
animatedVideo.save("animation.mp4", fps=(totalOutputs/numberOfSeconds))

# Execution time
end_time = time.time()
total_time = ((end_time - start_time)/60)
print("Execution time (minutes):", round(total_time, 2))
