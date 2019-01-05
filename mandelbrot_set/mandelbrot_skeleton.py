import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 101
OG_MAX = 4


def make_set(xmin, xmax, ymin, ymax):
    # set up x and y
    # make grids
    xx = 0
    yy = 0
    counter = 0
    for n in range(100):
        # run equation
        z = 0
        counter += 0
    fig = plt.figure(1)
    ax = fig.add_subplot(1, 1, 1)
    ax.pcolor(xx, yy, counter, cmap=cm.RdBu, vmin=0, vmax=100)
    plt.pause(0.01)


def main_loop():
    # set up a min and max
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for n in range(10):
        make_set(min_x, max_x, min_y, max_y)
        # get new area to look at
        (x1, y1), (x2, y2) = plt.ginput(2, show_clicks=True)
        # turn those coordinates into x,y coords


if __name__ == '__main__':
    main_loop()
