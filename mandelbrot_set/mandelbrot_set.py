import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 101
OG_MAX = 4


def make_set(xmin, xmax, ymin, ymax):
    x = np.linspace(xmin, xmax, RESOLUTION)
    y = np.linspace(ymin, ymax, RESOLUTION) * 1j
    xx, yy = np.meshgrid(x, y)
    counter = np.zeros(xx.shape)
    ogz = xx + yy
    z = xx + yy
    for n in range(100):
        z = z ** 2 + ogz
        total = np.absolute(z)
        counter += total < 2
        z[total > 2] = 100
    fig = plt.figure(1)
    ax = fig.add_subplot(1,1,1)
    ax.pcolor(xx, yy, counter, cmap=cm.RdBu, vmin = 0, vmax=100)
    plt.pause(0.01)


def main_loop():
    min_x, max_x, min_y, max_y = -OG_MAX / 2, OG_MAX / 2, -OG_MAX / 2, OG_MAX / 2

    for n in range(10):
        x_range = max_x - min_x
        y_range = max_y - min_y
        make_set(min_x, max_x, min_y, max_y)
        (x1, y1), (x2, y2) = plt.ginput(2, show_clicks=True)
        old_min_x = min_x
        old_min_y = min_y
        min_x = old_min_x + min(x1, x2) * x_range / RESOLUTION
        max_x = old_min_x + max(x1, x2) * x_range / RESOLUTION
        min_y = old_min_y + min(y1, y2) * y_range / RESOLUTION
        max_y = old_min_y + max(y1, y2) * y_range / RESOLUTION

    a = 0


if __name__ == '__main__':
    main_loop()
