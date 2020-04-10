from typing import List

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fig: plt.Figure
plot: plt.Axes
plot_list: List[plt.Axes]
plot_grid: List[List[plt.Axes]]

fig, plot = plt.subplots()
plot.hist(np.random.randn(100), bins=np.linspace(0, 1, 100))

fig, plot_grid = plt.subplots(nrows=2, ncols=2)
fig, plot_list = plt.subplots(nrows=2)
fig, plot_list = plt.subplots(ncols=2)
fig, plot_grid = plt.subplots(squeeze=False)
fig, plot_grid = plt.subplots(nrows=2, squeeze=False)
fig, plot_grid = plt.subplots(ncols=2, squeeze=False)
fig, plot_grid = plt.subplots(nrows=2, ncols=2, squeeze=False)
plt.xticks(ticks=[0, 1], labels=["foo", "bar"])
plt.yticks(ticks=[0, 1], labels=["foo", "bar"])
plt.xticks(ticks=np.array([0, 1]), labels=np.array(["foo", "bar"]))
plt.xticks(ticks=pd.Series([0, 1]), labels=pd.Series(["foo", "bar"]))
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.fill_between((0, 1), y1=(0, 1), y2=(1, 1), where=[True], interpolate=False, data=[])
