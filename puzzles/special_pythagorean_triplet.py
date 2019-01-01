"""
(009)
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2  (x**y means x to the yth power)
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
def triplet():
    a = 0
    b = 0
    c = 0

    for a in range(0, 1001):
        for b in range(a+1, 1001):
            for c in range(b+1, 1001):
                if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                    print("{},{},{}".format(a, b, c))
    return 0

triplet()
print("Done")
