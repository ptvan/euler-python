# Project Euler problem 022
# given a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

# pretty straightforward: create the score dict using comprehension
# then just add the scores to a grand total as we enumerate() through
import csv
import numpy as np

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = list(np.arange(1, 27))
scores = {alpha[i]: score[i] for i in range(len(alpha))}

with open('euler022_names.txt') as csv_file:
    names = list(csv.reader(csv_file, delimiter=','))[0]

total = 0
for ind, val in enumerate(names):
    tmp = 0
    for char in val:
        tmp += scores[char]
    print(val, total)
    total += tmp * (ind+1)

print(total)