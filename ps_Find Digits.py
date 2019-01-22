#Find Digits
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    chk=0
    for _ in n:
        try:
            if _!=0 and int(n)%int(_)==0:chk+=1
        except:pass
    return chk
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = input()
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
