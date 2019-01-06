"""
(005)
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solve_problem():
    num = 0
    notDiv = True
    count = 0
    while count < 20:
        num = num + 1
        count = 0
        for i in range(1, 21):
            if (num % i == 0):
                count += 1
    print("Final is {}".format(num))


# TODO: Discuss computational complexity

# Estimate Computational Complexity
def estimate_complexity(n):
    numbers = range(1, n + 1)
    smallest_known_multiple = 1
    for i in numbers:
        smallest_known_multiple *= i

    number_of_divisions = smallest_known_multiple * n
    print("total number of computer cycles for 1-{}: {}".format(n, number_of_divisions))


if __name__ == '__main__':
    for n in [5, 10, 15, 20, 25, 30]:
        estimate_complexity(n)
