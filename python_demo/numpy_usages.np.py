import numpy as np
from PIL import Image


# if you don't have PIL then have pycharm install the package "Pillow"


def select_value():
    my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # remember 0 indexing
    print("2nd row, 2nd column value is: {}".format(my_array[1, 1]))

    # you can also select multiple at a time
    rows = [0, 1, 2]
    cols = [0, 1, 2]
    print("The diagonal values are {}".format(my_array[rows, cols]))


def find_shape():
    my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    width, height = my_array.shape
    print("The array has {} columns and {} rows".format(width, height))


def make_new_arrays():
    array_of_zeros = np.zeros([10, 10, 10])
    np.ones([10, 10, 10])
    another_array_of_ones = np.ones_like(
        array_of_zeros)  # this one will be the same size


def slice_array():
    """Slicing an array is taking some smaller array from inside of a larger array. It will
    return a numpy array"""
    img = Image.open("flamingo.jpg")
    image_as_array = np.array(img)
    width, height, depth = image_as_array.shape

    red_channel = image_as_array[:, :, 0]
    green_channel = image_as_array[:, :, 1]
    blue_channel = image_as_array[:, :, 2]

    top_left_corner = image_as_array[:height // 2, :width // 2, :]
    top_right_corner = image_as_array[:height // 2, width // 2:, :]
    random_middle_pixels = image_as_array[11:29, 101:400, :]


def iterating_over_array():
    my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    width, height = my_array.shape
    for row in range(height):
        for col in range(width):
            print("{} ".format(my_array[row, col]))

    print(" ")
    for row in range(height):
        print("{} {} {} ".format(my_array[row, 0],
                                 my_array[row, 1],
                                 my_array[row, 2]))


if __name__ == '__main__':
    select_value()
    find_shape()
    iterating_over_array()
