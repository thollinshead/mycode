#!/usr/bin/env python3

## Script to search and find all matches

import os

## Define a function that cat

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

lookfor = input("what am I looking for? ")
lookwhere = input("what is the path in which I should search? ")

print(find_all(lookfor, lookwhere))
