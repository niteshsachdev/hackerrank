#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    dict1=dict(Counter(ar))
    max1=max(ar)
    return dict1[max1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
