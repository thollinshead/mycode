#!/usr/bin/env python3
message = 'Which package based on Favorite Channel Number?'
hostname = int(input("Favorite Channel Number"))
if hostname in range(1,10):
    print("Basic")
elif hostname in range(10,40):
    print("Standard")
elif hostname in range(40,100):
    print("Premium")
elif hostname in range (101,200):
    print("HD")
elif hostname in range (201,600):
    print("Expensive Extras")
