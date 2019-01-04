"""
(003)
The prime factors of 13195 are 5, 7, 13 and 29.
find all the numbers it's divisible by
filter to prime terms only
find the larges prime value left
What is the largest prime factor of the number 600851475143 """

num = 600851475143
div = 0
prime = 0
isPrime = True

for i in range(1, num):
    if num % i == 0:
        div = i
        for j in range(2, div):
            if j % div == 0:
                isPrime = True
            elif div % j == 0:
                isPrime = False
        if isPrime:
            if div > prime:
                prime = div
                print("prime is changed to {}".format(prime))

print(prime)

# TODO: Talk about limits math.sqrt(div)
