#!/bin/env python

# project euler problem 3
# seen from projecteuler.net


import math


x = 600851475143

# find square root to know when we can stop looking for factors

squareroot = math.sqrt(x)

print("squareroot is %d" % squareroot)


def is_factor(n,x):
    """ Returns whether or not n is a factor of x? """
    if x % n == 0:
        return True
    else:
        return False

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    
    

i=2
factor_list = [1,2]


while i < squareroot:
    if squareroot % i == 0 and is_prime(i):
        # prime factor
        factor_list.append(i)
    i+=1
    print(factor_list)
print("LPF of %d is %d" % (x,max(factor_list)))
