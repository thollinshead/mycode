#!/usr/bin/env python3
message = 'Which package based on Favorite Channel Number?'
hostname = int(input("Favorite Channel Number"))
favs = ['26', '52', '4', '498', '102']
for f in favs:
    print(f)
    if hostname in range(1,10):
        print("Basic")
        break
    elif hostname in range(11,40):
        print("Standard")
        break
    elif hostname in range(41,100):
        print("Premium")
        break
    elif hostname in range (101,200):
        print("HD")
        break
    elif hostname in range (201,600):
        print("Expensive Extras")
        break
