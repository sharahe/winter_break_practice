"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                        75
                       95 64
                     17 47 82
                   18 35 87 10
                  20 04 82 47 65
                19 01 23 75 03 34
               88 02 77 73 07 63 67
             99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)"""


import numpy as np

def check_grid(grid):
    count = 0
    i = 0
    j = 0
    current = grid[i, j]
    sum = current
    print("initial sum is {}".format(sum))
    while(count < 14):
            print("currently {}".format(current))
            if(grid[j+1, i] > grid[j+1, i+1]):
                print("initially lower now is {}".format(grid[j+1, i]))
                sum = sum + grid[j+1, i]
                print("sum {}".format(sum))
                current = grid[j+1, i]

            else:
                print("the right  is lower now {}".format(grid[j+1, i+1]))
                sum = sum + grid[j+1, i+1]
                print("sum right {}".format(sum))
                current = grid[j+1, i+1]
                i += 1
            count += 1
            j += 1
            print(count)
    return sum

if __name__ == '__main__':
    pyramid = np.array([[75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [95, 64,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [17, 47, 82,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [18, 35, 87, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [20,  4, 82, 47, 65,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [19,  1, 23, 75,  3, 34,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [88,  2, 77, 73,  7, 63, 67,  0,  0,  0,  0,  0,  0,  0,  0],
                        [99, 65,  4, 28,  6, 16, 70, 92,  0,  0,  0,  0,  0,  0,  0],
                        [41, 41, 26, 56, 83, 40, 80, 70, 33,  0,  0,  0,  0,  0,  0],
                        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29,  0,  0,  0,  0,  0],
                        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,  0,  0,  0,  0],
                        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,  0,  0,  0],
                        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,  0,  0],
                        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,  0],
                        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]])

    print("Largest Sum: {}".format(check_grid(pyramid)))
    print(75+95+47+87+82+75+73+28+83+47+43+73+91+67+98)

    # TODO: you got lucky. I will check this myself later
