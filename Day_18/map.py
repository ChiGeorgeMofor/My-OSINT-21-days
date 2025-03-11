import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(22, 22))

map = Basemap()

map.drawcountries()
map.drawcoastlines()

map.plot(13.4, 52.52, 'ro', markersize=10)

plt.title("World map", fontsize=20)

plt.savefig('map.png')