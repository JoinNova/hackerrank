'''
###day4
class Person:
    def __init__(self,age):
        self.age=age
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age < 0:
            print('Age is not valid, setting age to 0.')
            self.age=0
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else: 
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1
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
'''
'''
###day6
from sys import stdin
for i in range(int(stdin.readline())):
    a=str()
    b=str()
    s=stdin.readline().strip()
    for j in range(len(s)):
        if j%2==0:
            a+=s[j]
        else:
            b+=s[j]
    print(''.join(a),''.join(b))
            
'''
'''
###07
#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())

    arr = list(map(str, input().rstrip().split()))
    print(' '.join(arr[::-1]))
'''
###08
'''
from sys import stdin
l={}
for i in range(int(stdin.readline().strip())):
    k,val=map(str,stdin.readline().split())
    l[k]=val
for i in range(len(l)):
    k=stdin.readline().strip()
    try:
        print('{0}={1}'.format(k,l[k]))
    except:
        print('Not found')
'''
'''
from sys import stdin
l={}
result=[]
n=int(stdin.readline().strip())
for i in range(n):
    k,val=map(str,stdin.readline().split())
    l[k]=int(val)
for i in range(n):
    k=stdin.readline().strip()
    if k in l.keys():
        #print('{0}={1}'.format(k,l.get(k)))
        result.append('{0}={1}'.format(k,l.get(k)))
    else:
        #print('Not found')
        result.append('Not found')
print('\n'.join(result))
'''
'''
T = int(input())
d = {}
for i in range(T):
    text = input().split(" ") 
    d[text[0]] = text[1]

for i in range(T):
    st = input()
    if st in d.keys():
        print('{}={}'.format(st,d[st]))
    else: print("Not found")
'''
'''
#day10
r=0
result=0
for _ in bin(int(input()))[2:]:
    if _=='1':
        r+=1
    else:
        r=0
    result=max(result,r)
print(result)
'''
'''
###day11
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    m=0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            if i==0 and j==0:
                m=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            else:
                m=max(m,arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        
    print(m)
'''
'''
###day12
class Person:
	def __init__(self, firstName, lastName, idNum):
		self.firstName = firstName
		self.lastName = lastName
		self.idNum = idNum
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNum)

class Student(Person):        
        def __init__(self,firstName,lastName,idNum,scores):                               
                self.firstName = firstName
                self.lastName = lastName
                self.idNum = idNum
                self.scores = scores
        def calculate(self):
                avg=sum(self.scores)/len(self.scores)
                if avg>=90:return 'O';
                elif avg>=80:return 'E';
                elif avg>=70:return 'A';
                elif avg>=55:return 'P';
                elif avg>=40:return 'D';
                else:return 'T';



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
'''


###013
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class MyBook:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def MyBook(self):
        result=str()
        result+='Title: '+self.title+'\n'
        result+='Author: '+self.author+'\n'
        result+='Price: '+self.price
        return result
            
#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
