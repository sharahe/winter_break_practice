"""
(004)
A palindromic number reads the same both ways. The largest palindrome made from
 the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import collections

product = 0
pal = collections.deque()
strnum = ""
isPal = True
largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        strnum = str(product)
        isPal = True
        front = 0
        back = -1
        while (isPal and front < len(strnum)):
            if (strnum[front] == strnum[back]):
                front += 1
                back -= 1
            else:
                isPal = False
        if (isPal):
            if product > largest:
                largest = product
        print("current largest is {}".format(largest))

