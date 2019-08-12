
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    sum1=int((reduce((lambda x,y:x+y),bill))/2)
    if b== sum1:
        print("Bon Appetit")
    else:
        print(int(abs(b-sum1)))



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
