#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def lastDigit(number):
    return(number % 10)

if number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastDigit(number)))
if number < 6 and number != 0:
    print("Last digit of {:d} is {:d} and is less than 6".format(number, -lastDigit(-number)))
if number == 0:
    print("Last digit of {:d} is {:d} and is zero".format(number, lastDigit(number)))
