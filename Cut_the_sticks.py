

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res=[]
    arr.sort(reverse=True)
    while len(arr)>0:
        res.append(len(arr))
        min_n=min(arr)
        while min_n in arr:
            arr.pop()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
