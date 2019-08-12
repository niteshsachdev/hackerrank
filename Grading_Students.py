#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def round_grade(marks):
    if marks < 38:
        return marks
    elif (5*round(marks/5)-marks)>0 and (5*round(marks/5)-marks)<3:
        return (5*round(marks/5))
    elif (5*round(marks/5)-marks)==3:
        return marks
    else:
        return marks

def gradingStudents(grades):
    res=list(map(lambda x:round_grade(x),grades))
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
