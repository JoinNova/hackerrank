#!/bin/python3

from math import*
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    r=n//c
    x=r
    while x//m>0:
        y=x//m
        x-=y*m
        x+=y
        r+=y
    return r
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        print(result)
        #fptr.write(str(result) + '\n')
    #fptr.close()
