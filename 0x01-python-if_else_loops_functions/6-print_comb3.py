#!/usr/bin/python3
combo = 0
while combo <= 89:
    if combo % 10 == 0:
        combo += 1 + combo // 10
    print("{:02d}".format(combo), end="\n" if combo == 89 else ", ")
    combo += 1
