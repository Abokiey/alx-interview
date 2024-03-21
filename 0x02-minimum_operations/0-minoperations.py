#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """calculate the fewest no. of operations needed"""
    if n <= 1:
      return 0
    
    operations = 0
    i = 2
    
    while n > 1:
        if n % i == 0:
            operations += i
            n = n / i
        else:
            i += 1
    return operations