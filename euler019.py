# Project Euler problem 019
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# using libraries, this is rather straightforward
# we keep a counter of the day-of-week of all the first days of the month


from datetime import date
from collections import Counter

counts = Counter()

for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        counts[day.weekday()] += 1

print(counts[6])

