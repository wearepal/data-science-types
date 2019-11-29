from matplotlib import pyplot as plt
import numpy as np

fig: plt.Figure
plot: plt.Axes

fig, plot = plt.subplots()
plot.hist(np.random.randn(100), bins=np.linspace(0, 1, 100))
