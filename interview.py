'''
###003Repeated String
import math
import os
import random
import re
import sys
# Complete the repeatedString function below.
def repeatedString(s, n):
    x=n//len(s)
    y=n%len(s)
    return s.count('a')*x+s[:y].count('a')
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
'''
'''
###004Jumping on the Clouds
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    j=0
    s=0
    while s<len(c)-1:
        if (s+2)<len(c):
            if c[s+2]!=1:
                s+=2
                j+=1
            else:
                s+=1
                j+=1
        else:
            s+=1
            j+=1
    return j
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
'''
'''
###005_2D Array - DS
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the hourglassSum function below.
def hourglassSum(arr):
    ar=[]
    for i in range(4):
        for j in range(4):
            ar.append(\
                arr[i][j]+arr[i][j+1]+arr[i][j+2]+\
                    arr[i+1][j+1]+\
                        arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])       
    return max(ar)
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
'''
'''
###Day 1: Data Types
i = 4
d = 4.0
s = 'HackerRank '
print('%d'%(i+int(input())))
print('%0.1f'%(d+float(input())))
print('%s'%(s+input()))
'''
'''
###problem solving030
import math
import os
import random
import re
import sys
# Complete the reverseArray function below.
def reverseArray(a):
    return reversed(a)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
    #fptr.write(' '.join(map(str, res)))
    #fptr.write('\n')
    #fptr.close()
'''
'''
###problem solving031
import math
import os
import random
import re
import sys
def dynamicArray(n, queries):
    s0=[]
    s1=[]
    last=0
    for _ in queries:
        _[0]
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nq = input().rstrip().split()
    n = int(nq[0])
    q = int(nq[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()
'''
'''
###
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost+meal_cost*tip_percent/100+meal_cost*tax_percent/100))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
'''

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
