#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    res=0
    for ch in range(len(s)):
        count=0
        sum_n=0
        while count<m:
            sum_n+=s[ch+count]
            count+=1
        if sum_n==d:
            res+=1
        if(ch+count==len(s)):
            break
    return res
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()