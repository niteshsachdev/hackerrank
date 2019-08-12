#!/bin/python3

import math
import os
import random
import re
import sys

def current(d,side):
    if side=='U':
        return d-1
    else:
        return d+1
    
# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    curr=0
    for step in s:
        if step=='U':
            curr+=1
            if curr==0:
                count+=1
        else:
            curr-=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()