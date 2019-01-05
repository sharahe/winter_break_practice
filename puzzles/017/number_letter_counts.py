"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
 contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.
 answer: 21124"""

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  # 36
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"]  # 70
dec = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  # 46
"""hundreds = ["onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred",
            "eighthundred", "ninehundred"]  # 99"""

# sum of the lengths in ones (1-9)
sumOnes = 0
for i in range(0, len(ones)):
    sumOnes += len(ones[i])
# sum of 10-19
sumTens = 0
for i in range(0, len(tens)):
    sumTens += len(tens[i])
# sum of the decs (20,30,40,...)
sumDecs = 0
for i in range(0, len(dec)):
    sumDecs += len(dec[i])
# sum of the rest of the decs (21-29)(31-39).....99)
sumSets = 0
sum = 0
for i in range(0, len(dec)):
    sumSets = (10 * sumDecs) + (8 * sumOnes)
    sum = sumSets + sumOnes + sumTens

finalSum = sum + (sumOnes * 100) + (sum * 9) + (len("hundred") * 9) + (len("hundredand") * 99 * 9) + len("onethousand")
print(finalSum)

