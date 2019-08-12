#!/bin/python3

import math
import os
import random
import re
import sys
 
# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples=list(map(lambda x:a+x,apples))
    oranges=list(map(lambda x:b+x,oranges))
    apple,orange=0,0
    for i in apples:
        if i in range(s,t+1):
            apple+=1
    for i in oranges:
        if i in range(s,t+1):
            orange+=1
    print(apple)
    print(orange)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
