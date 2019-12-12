# Project Euler problem 017
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


singles = ["",
           "one",
           "two",
           "three",
           "four",
           "five",
           "six",
           "seven",
           "eight",
           "nine",
           "ten"]

teens = ["ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen"]

tens = ["",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]

length = 0
string = ""

for i in range(1, 1001):
    if i < 11:
        string = singles[i]

    if 11 <= i < 20:
        string = teens[i - 10]

    if i == 20:
        string = "twenty"

    if 21 <= i < 100:
        digits = list(str(i))
        string = tens[int(digits[0]) - 1] + " " + singles[int(digits[1])]

    if i == 100:
        string = "one hundred"

    if 100 < i < 1000:
        digits = list(str(i))
        if int(digits[1]) == 0:
            string = singles[int(digits[0])] + " hundred " + singles[int(digits[2])]
        if int(digits[1]) == 1:
            string = singles[int(digits[0])] + " hundred " + teens[int(digits[2])]
        if int(digits[1]) >= 2:
            string = singles[int(digits[0])] + " hundred " + tens[int(digits[1]) - 1] + " " + singles[int(digits[2])]

    if i == 1000:
        string = "one thousand"

    # print(i, string)
    length = length + len(string)

print(length)
