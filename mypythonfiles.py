#!/usr/bin/env python3

import os
import pyexcel
import fnmatch

path = "."

file = os.listdir(path)

for file in os.listdir():
    if file.endswith(".py"):
        print(file)

mylist = []

def write_excel(mylist):
    for name in file:
        des = input('What description do you want to add ')
        prog = {"Filename": name, "Des": des}
        print(prog)

write.excel(file)

    
