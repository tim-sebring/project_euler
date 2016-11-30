#!/bin/env python

# Project euler problem #2, projecteuler.net


def next_fib(a,b):
    return a + b

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

sum = 2  # starting with first even number added to sum

# set the starting terms
term1 = 1
term2 = 2
newterm = 0

while term2 < 4000000:
    newterm = next_fib(term1,term2)
    if is_even(newterm):
        sum += newterm
    term1=term2
    term2=newterm


print("Sum of even numbers are %d" % sum)
