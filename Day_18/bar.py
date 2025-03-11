import matplotlib.pyplot as plt 
import numpy as np

x = np.array(["Los Angeles", "New York", "Chicago", "Houston", "Phoenix"])
y = np.array([3.8, 8.4, 2.7, 666.3, 1.6])

plt.bar(x, y)

plt.title("Population")

plt.savefig("population_barchart.png")