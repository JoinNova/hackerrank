#Day 26: Nested Logic
# Enter your code here. Read input from STDIN. Print output to STDOUT

from datetime import date
day0,month0,year0=map(int,input().split())
day1,month1,year1=map(int,input().split())
if (date(year0,month0,day0)-date(year1,month1,day1)).days>0:
    if year0>year1:print(10000)
    else:
        if month0>month1:print(500*(month0-month1))
        else:
            if day0>day1:print(15*(day0-day1))
            else:print(0)

else:print(0)
