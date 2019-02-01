#ps_maxmin_nova
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    ar=arr
    ar.sort()
    re=10**5*k
    for _ in range(len(ar)-k+1):
        re=min(re,ar[_+k-1]-ar[_])
    return re
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
