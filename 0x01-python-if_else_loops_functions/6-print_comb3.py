#!/usr/bin/python3
combo = []
for i in range(10):
    for j in range(10):
        if (i != j and i < j):
            print(f"{i}{j}", end='\n' if combo == 89 else ", ")
