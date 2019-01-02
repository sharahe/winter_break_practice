"""
(007)
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
num = 2
count = 0
prime = 0
isPrime = True
list = []
while count < 10001 and isPrime:
    for i in range(2, num + 1 ):
        if isPrime:
            if num % i == 0:
                if num == i:
                    isPrime = True
                else:
                    isPrime = False
    if isPrime:
        list.append(num)
        count = count + 1
    num = num + 1
    isPrime = True
print(list)
print(list[10000])
