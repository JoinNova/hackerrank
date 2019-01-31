#day20_Sort_Nova
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap=0
for i in range(n-1):
    for j in range(n-1):
        if a[j]>a[j+1]:
            swap+=1
            a[j],a[j+1]=a[j+1],a[j]


print('Array is sorted in %d swaps.\nFirst Element: %d\nLast Element: %d'%(swap,a[0],a[-1]))
