#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if lastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, number % 10))
if lastDigit < 6 and not(lastDigit == 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, -lastDigit))
if lastDigit == 0:
    print("Last digit of {:d} is {:d} and is zero".format(number, lastDigit))
