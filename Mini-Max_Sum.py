#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
def sum_no(list1):
    res =reduce((lambda x,y:x+y),list1)
    return res
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr=sorted(arr)
    min1=arr[:-1]
    max1=arr[1:]
    print(sum_no(min1),sum_no(max1))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
