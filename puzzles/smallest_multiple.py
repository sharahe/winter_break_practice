"""
(005)
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
num = 0
notDiv = True
count = 0
while count < 20:
    num = num + 1
    count = 0
    for i in range(1, 21):
        if(num % i == 0):
            count += 1
print("Final is {}".format(num))
