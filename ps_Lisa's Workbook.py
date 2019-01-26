#Lisa's Workbook
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    r=0;a=1
    for _ in arr:
        l=list(range(1,_+1))
        chk=0
        for i in range(_//k+1 if _%k>0else _//k):
            #print(i,l[chk:chk+k])
            if l[chk:chk+k].count(a):r+=1
            a+=1;chk+=k
    return r

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
