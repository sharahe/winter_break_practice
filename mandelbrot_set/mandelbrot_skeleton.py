import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 101
OG_MAX = 4


def make_set(xmin, xmax, ymin, ymax):
    # linspace is a very useful function for making a bunch of evenly spaced numbers
    # ex. to get 10 numbers between 0 and 1 you say: x = np.linspace(0,1,10)

    # [Make x a list of RESULUTION numbers between xmin and xmax]
    x = None

    # [Make y a list of RESULUTION numbers between ymin and ymax]
    y = None
    # the y axis represents imaginary numbers, so here is how we make y imaginary
    y = y * 1j

    # x and y are only 1D, so to calculate a function over all possible x,y combinations you would
    # need to loop over them 1 by 1 (snorefest). Numpy is great because if you write your functions
    # correctly, it will do the math all at once (much faster). The first step in that process is to
    # make x and y into 2D matrices

    # To make them 2D, you can use a function called meshgrid.
    # x = np.array([1,2,3])
    # y = np.array([4,5,6])
    # xx,yy = np.meshgrid(x,y)
    # xx = 1 2 3
    #      1 2 3
    #      1 2 3
    #
    # yy = 6 6 6
    #      5 5 5
    #      4 4 4
    #
    # The result is that when you overlay xx and yy, every point has a unique set of x,y coordinates
    # like you are looking at a graph. If you have a function z = f(x,y), you can calculate z for
    # the whole area you are interested at once by calling f(xx,yy)

    # [Make xx and yy out of your x and y above]
    xx, yy = None

    # This guy will come in later
    counter = None

    for n in range(100):
        # The equation of the mandelbrot fractal is that th new z equals the
        # last z squared plus the original coordinates (xx+yy)

        # [Write the equation for z]
        z = None

        # what you are trying to count is the length of time it takes each z to get to
        # infinity. That sounds like too much work, we can count how long it takes to get
        # past 2

        # to get the absolute value of a complex number, you can call np.absolute(x)
        # [Get the absolute value of your Z]
        abs_val = None

        # Numpy has a lot of built in ways to compare. Conveniently with numpy arrays you
        # can just use >, <, >=, <=, == and it will give you True or false for the whole
        # array
        # [Get how many have an avsolute value > 2]
        greater_than_two = None

        # [Design some sort of counter to keep track of how everything is doing]
        counter += None

        # You will find out once you run the program that some of these values get really big really
        # fast. Numpy will start to get annoyed that you are asking it to deal with infinities. To
        # sidestep these concerns, you can keep values that you no longer care about small enough
        # not to cause issues.
        # "Masking" is a term that we use to only mess with certain values within an array easily
        # mask = np.array([[True False False],
        #                  [False True False],
        #                  [False False True]])
        # my_array = np.array([[1 1 1],
        #                      [1 1 1],
        #                      [1 1 1]])
        # my_array[mask]=9
        # print(my_array)  will give you:  9 1 1
        #                                  1 9 1
        #                                  1 1 9

        # [Assign all of z who's values are greater than 2, to 100]
        z[None] = 100

    plt.figure(1)
    plt.imshow(z, vmin=0, vmax=100)
    # This is a little trick I figured out. Sometimes python doesn't want to display a plot.
    # You can use plt.show() to force it to display, but then your program can't go on without
    # you doing extra things. plt.pause() will force it to show the plot. On the downside, if
    # your program ends before you can pause it some other way, the plot will exit, unlike
    # if you used plt.show()
    plt.pause(0.01)


def main_loop():
    # [set up a starting min and max of -2 to 2 for each]
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    for n in range(10):
        make_set(min_x, max_x, min_y, max_y)
        # This function will allow you to click on the image and record where you clicked. Until
        # that happens it will pause the program.
        (x1, y1), (x2, y2) = plt.ginput(2, show_clicks=True)

        # Now you have new coordinates that you want to zoom in on.
        # Problem 1) You don't know in what order someone clicked on the
        #            image.
        # [Figure out your mins and maxes again]
        min_pixel_x = None
        max_pixel_x = None
        min_pixel_y = None
        max_pixel_y = None

        # Problem 2) Coordinate systems!
        #            We displayed your fractal as an image with a certain resolution, NOT as a nice
        #            graph plot. Therefore, the coordinates you are getting back are in pixels.
        #            Given the image's resolution, and what you know it was displaying before, you
        #            can calculate what these pixel coordinates mean in x,y cartesian coordinates
        # [Translate pixel coordinates into x,y coordinates]
        min_x = None
        max_x = None
        min_y = None
        max_y = None

        # To make things pretty (this isn't really necessary, but it looks better), take your new
        # rectangular area and make it a square. This part is commented because you can do the rest
        # and come back to this one.

        # [make your image a square with sides equal to the largest side of your selection
        # rectangle]
        # min_x = None
        # max_x = None
        # min_y = None
        # max_y = None


if __name__ == '__main__':
    main_loop()
