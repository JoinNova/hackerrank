#day29_Bitwise AND
from math import*
import os
import random
import re
import sys
from itertools import combinations


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n,k = int(nk[0]),int(nk[1])

        top = int(log(n, 2)) - 1
        bottom = 2**top

        result = 0
        for i in range(bottom+1, n+1):
            for j in range(1, i):
                sub = i&j
                if sub > result and sub < k:
                    result = sub
            if result == k-1:
                break
        print(result)

#by asami_azeemi
import math
import os
import random
import re
import sys
import itertools


if __name__ == '__main__':
    t = int(input())

    Ns = []
    Ks = []
    Bits = {}
    for t_itr in range(t):
        nk = input().split()

        Ns.append(int(nk[0]))
        Ks.append(int(nk[1]))

    tuples = itertools.combinations(range(1,max(Ns)+1),2)
    for e in tuples:
        t = e[0] & e[1]
        if t in Bits:
            Bits[t].append(e)
        else:
            Bits[t] = [e]

    for idx,k in enumerate(Ks):
        bFound = False
        k -= 1
        while k >= 0:
            if k in Bits:
                for item in Bits[k]:
                    if item[0] <= Ns[idx] and item[1] <= Ns[idx]:
                        #found
                        bFound = True
                        break                
            if bFound:
                    break
            k -= 1
        if bFound or k==0:
            print(k)

#by maxvetrov555
from math import*
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n,k = int(nk[0]),int(nk[1])
        print(k-1-int((k-1|k)>n))
