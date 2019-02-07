#day28 RegEx, Patterns, and Intro to Databases
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    L=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        emailID = emailID.split('@gmail.com')
        #print(emailID)
        
        if firstName.islower()==True:
            if len(emailID)==2:
                if emailID[1]=='':
                    emailID=emailID[0]
                    if emailID.islower()==True:
                        L+=[firstName]
    print(*sorted(L),sep='\n')
