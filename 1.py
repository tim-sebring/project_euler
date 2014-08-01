#!/bin/env python


def is_mult_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

def is_mult_3(number):
    if number % 3 == 0:
        return True
    else:
        return False





sum = 0
i = 0

while i < 1000:
    if is_mult_5(i) or is_mult_3(i):
        sum += i
    i+=1

print("Sum is %d" % sum)
