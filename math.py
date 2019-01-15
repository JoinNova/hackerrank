'''
###040_Polar Coordinates
import cmath
n=input().split('j')
n=n[0]
if n.count('-')== 0:
    n=n.split('+')
    nn=int(n[0])
    m=int(n[1])
elif n.count('-')==1:
    if n[:1]=='-':
        n=n.split('+')
        nn=int(n[0])
        m=int(n[1])
    else:
        n.split('-')
        nn=int(n[0])
        m=-int(n[2])
else:
    n=n.split('-')
    nn=-int(n[1])
    m=-int(n[2])
print(abs(complex(nn, m)))
print(cmath.phase(complex(nn, m)))

###041_Find Angle MBC
import math
ab=int(input())
bc=int(input())
#print(ab*ab)
ac=math.sqrt(ab*ab+bc*bc)
#print(ac)
cm=ac/2
anglembc=math.acos((0.5*bc)/cm)
#print(anglembc)
mbcdegrees=math.degrees(anglembc)
print("{0}°".format(int(mbcdegrees)))
'''

