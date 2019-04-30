#!/usr/bin/python3
for cont in range(0, 89):
    if cont / 10 < cont % 10:
        print("{:02d},".format(cont), end=" ")
print("89")
