#https://www.hackerrank.com/domains/python?badge_type=python&filters%5Bsubdomains%5D%5B%5D=py-introduction
'''
###001_Say "Hello, World!" With Python
print("Hello, World!")

###002_Python If-Else
N=int(input())
if (N%2==0 and N>20) or (N%2==0 and N<6) : print("Not Weird") 
else : print("Weird")

###003_Arithmetic Operators
def plus(arg1,arg2):
    print(arg1+arg2)
def minus(arg1,arg2):
    print(arg1-arg2)
def multi(arg1,arg2):
    print(arg1*arg2)
if __name__ == '__main__' :
    a = int(input())
    b = int(input())
plus(a,b)
minus(a,b)
multi(a,b)

###004_Python: Division
def portion(arg1,arg2):
    print(arg1//arg2)
def div(arg1,arg2):
    print(arg1/arg2)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
portion(a,b)
div(a,b)

###005_Loops
def Loops(arg):
    for _ in range(arg):
        print(_*_)
if __name__ == '__main__' :
    Loops(int(input()))

###006_Write a function
def is_leap(year):
    leap = False
    if (year%4==0 and year%100!=0) or (year%4==0 and year%400==0):
        leap = True
    return leap
if __name__ == '__main__' :
    year = int(input())
    print(is_leap(year))
'''
###007_Print Function
def order(arg):
    for _ in range(arg):
        print(_+1,end='')    
if __name__ == '__main__':
    order(int(input()))
