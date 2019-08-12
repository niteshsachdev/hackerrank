#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def pickingNumbers(a):
    a=sorted(a)
    dis=sorted(list(set(a)))
    dif=dict(Counter(a))
    res=0
    for i in range(len(dis)-1):
        if (dis[i+1]-dis[i])<=1:
            get=dif[dis[i+1]]+dif[dis[i]]
            if get>res:
                res=get
    for key,values in dif.items():
        if values>res:
            res=values
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()