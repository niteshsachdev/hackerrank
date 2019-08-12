    
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    #one method of solving
    """fact=1
    while(n!=0):
        fact=fact*n
        n-=1
    print(fact)"""
    #another method of solving
    print(math.factorial(n))

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)