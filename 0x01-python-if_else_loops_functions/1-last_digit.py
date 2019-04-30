#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    dig = (number * -1) % 10
    if dig > 0:
        print("Last digit of {:d} is -{:d} and is less than 6 and not 0"
          .format(number, dig))
    else:
        print("Last digit of {:d} is {:d} and is 0".format(number, dig))
else:
    dig = number % 10
    if dig == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, dig))
    elif dig > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, dig))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, dig))
