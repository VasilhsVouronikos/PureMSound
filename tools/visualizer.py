import matplotlib.pyplot as plt
import numpy as np


def visualize(line,data,fig):
	line.set_ydata(data)
	fig.canvas.draw()
	fig.canvas.flush_events()
	return

def init_vis(CHUNK):
	fig, ax = plt.subplots(figsize=(14,6))
	x = np.arange(0, 2 * CHUNK, 2)
	ax.set_ylim(-200, 200)
	ax.set_xlim(0, CHUNK) #make sure our x axis matched our chunk size
	line, = ax.plot(x, np.random.rand(CHUNK))

	return x,fig,ax,line