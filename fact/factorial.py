#!/usr/bin/env python3
# user input 
x = int(input("Enter a number: "))
f = 1
# edited x into x+1
for i in range(1, x+1):
    f = f * i
    print(x, "! =  ", f)

