"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def fibon_sum():
    sum = 0
    valOne = 1
    valTwo = 2
    newVal = 0
    sum += valTwo
    while newVal < 3524577:
        newVal = valOne + valTwo
        if (newVal % 2 == 0):
            print("newVal: {}".format(newVal))
            sum += newVal
            print("sum: {}".format(sum))
        valOne = valTwo
        valTwo = newVal

fibon_sum()
