#https://www.hackerrank.com/domains/python?badge_type=python&filters%5Bsubdomains%5D%5B%5D=py-strings
'''
###014_sWAP cASE
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__' :
    s = input()
    result = swap_case(s)
    print(result)

###015_String Split and Join
def split_and_join(line):
    return "-".join(line.split())
if __name__ == '__main__' :
    line = input()
    result = split_and_join(line)
    print(result)

###016_What's Your Name?
def print_full_name(a,b):
    print('Hello {0} {1}! You just delved into python.'.format(a,b))
if __name__ == '__main__' :
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

###017_Mutations
def mutate_string(string, position, character):
    #return string[:position] + character + string[position+1:]
    l=list(string)
    l[position] = character
    return ''.join(l)
if __name__ == '__main__' :
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

###018_Find a string
def count_substring(string, sub_string):
    chk=0
    for i in range(len(string)-len(sub_string)+1):
        #if string[i:i+len(sub_string)] == sub_string:
        chk+=string[i:i+len(sub_string)] == sub_string
    return chk

if __name__ == '__main__' :
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
   
###018_Find a string
def count_substring(string, sub_string):
    chk=0
    for i in range(len(string)-len(sub_string)+1):
        chk+=string.count(sub_string, i, i+len(sub_string))
    return chk
if __name__ == '__main__' :
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

###019_String Validators
if __name__ == '__main__':
    s = input()
    a,b,c,d,e = [],[],[],[],[]
    for _ in s:
        a.append(_.isalnum())
        b.append(_.isalpha())
        c.append(_.isdigit())
        d.append(_.islower())
        e.append(_.isupper())
    print("{0}\n{1}\n{2}\n{3}\n{4}".format(any(a),any(b),any(c),any(d),any(e)))

###020_Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

###021_Text Wrap
import textwrap
def wrap(string,max_width):
    result=str()
    for i in range(0,len(string),max_width):
        result+=string[i:i+max_width]+"\n"
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

###
import textwrap
def wrap(string,max_width):
    return textwrap.fill(string,max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

###022_Designer Door Mat
n,m = list(map(int,input().split()))
for i in range(1,n,2):
    print((".|."*i).center(m,'-'))
print(("WELCOME").center(m,'-'))
for i in range(n-2,0,-2):
    print((".|."*i).center(m,'-'))

###23_String Formatting
def print_formatted(n):
    for i in range(n):
        print(str(i+1).rjust(len(bin(n)[2:]),' '),(oct(i+1)[2:]).rjust(len(bin(n)[2:]),' '),(hex(i+1)[2:].upper()).rjust(len(bin(n)[2:]),' '),(bin(i+1)[2:]).rjust(len(bin(n)[2:]),' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

###024_Alphabet Rangoli
def print_rangoli(n):
    p='abcdefghijklmnopqrstuvwxyz'
    for i in range(n):
        lp=str()
        for j in range(i+1):
            lp+=p[n-j-1]+'-'
        total=lp.rjust(n*2+1,'-')+lp[::-1][3:].ljust((n-1)*2,'-')
        print(total[1:len(total)-1])
    for i in range(n-1):
        lp=lp[:len(lp)-2]
        total=lp.rjust(n*2+1,'-')+lp[::-1][3:].ljust((n-1)*2,'-')
        print(total[1:len(total)-1])
if __name__=='__main__':
    n = int(input())
    print_rangoli(n)

###공부해야됨.
def gen(n):
    for i in range(n * 2 - 1):
        yield n - abs(i - n + 1)        
n = int(input())
for i in gen(n):
    print('-'.join(chr(ord('a') + n - j) for j in gen(i)).center(n * 4 - 3, '-'))

###025_Capitalize!
import math
import os
import random
import re
import sys
def solve(s) :
    ss=str()
    chk=0
    for i in range(len(s)):
        if s[i]==' ':
            chk+=1
            ss+=s[i]
        elif i==0 or (chk>0 and s[i]!=' '):
            ss+=s[i].capitalize()
            chk=0           
        else:
            ss+=s[i]
    return ss

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

###
s=input()
s=s.split(' ')
sss=str()
for i in s:
    i=i.capitalize()
    for _ in i:
        sss+=_
    sss+=' '
print(sss)

###
s = input()
for _ in s[:].split():
    s = s.replace(_, _.capitalize())
print(s)

###026_The Minion Game
from re import search
def minion_game(s):
    v = {'A','E','I','O','U'}
    stu=0
    ke=0
    for i in range(len(s)):
        if s[i] in v:
            ke += len(s) - i
        else :
            stu += len(s) - i

    if stu>ke:
        print('Stuart',stu)
    elif stu<ke:
        print('Kevin',ke)
    else :
        print('Draw')  
    
if __name__ == '__main__' :
    s = input()
    minion_game(s)
'''

###027_Merge the Tools!
def merge_the_tools(s,k):
    for i in range(0,len(s),k):
        sss=str()
        ss=s[i:i+int(k)]
        for _ in ss:
            if sss.count(_)==0:
                sss+=_
        print(sss)
     

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string,k)

