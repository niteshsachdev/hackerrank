
#!/bin/python3

import math
import os
import random
import re
import sys

# one way of sloving
"""
def short(n,y):
    new_res=[n*n]
    n+=1
    while n*n<=y:
        new_res.append(n*n)
        n+=1
    return new_res

def squares(a, b):
    res=[]
    for i in range(a,b+1):
        r=int(math.sqrt(i))
        if r*r==i:
            res=short(r,b)
            break
    return len(res)
"""
#another way of solving

def squares(a, b):
    count=math.floor(math.sqrt(b))-math.floor(math.sqrt(a-1))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()