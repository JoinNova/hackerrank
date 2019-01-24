#Is Fibo
#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    a,b=0,1
    while b<=n+1:
        a,b=b,a+b
        if b==n:
            return 'IsFibo'
    return 'IsNotFibo'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = solve(n)
        print(result)
        #fptr.write(result + '\n')
    #fptr.close()
