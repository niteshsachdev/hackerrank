
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    greater_value,lower_value=scores[0],scores[0]
    greater,lower=0,0
    for sc in scores:
        if lower_value>sc:
            lower+=1
            lower_value=sc
        if sc>greater_value:
            greater+=1
            greater_value=sc
    return [greater,lower]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
