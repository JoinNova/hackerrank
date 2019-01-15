'''
###027_Introduction to Sets
def average(array):
    return sum(list(set(array)))/len(list(set(array)))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

###028_Symmetric Difference
n=int(input())
nl=set(map(int, input().split()))
m=int(input())
ml=set(map(int, input().split()))
result=sorted(ml.symmetric_difference(nl))
for _ in result:
    print(_)

###029_Set .add()
nl=[]
for i in range(int(input())):
    nl.append(input())
print(len(set(nl)))


###030_Set .discard(), .remove() & .pop()
n=int(input())
nl=set(map(int, input().split()))
for i in range(int(input())):
    cmd=input().split()
    if cmd[0] == 'remove':
        nl.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        nl.discard(int(cmd[1]))
    else:
        nl.pop()
print(sum(nl))

###031_Set .union() Operation
n=int(input())
nl=set(map(int,input().split()))
m=int(input())
ml=set(map(int,input().split()))
print(len(nl.union(ml)))

###032_Set .intersection() Operation
n=int(input())
nl=set(map(int,input().split()))
m=int(input())
ml=set(map(int,input().split()))
print(len(nl.intersection(ml)))

###033_Set .difference() Operation
n=int(input())
nl=set(map(int,input().split()))
m=int(input())
ml=set(map(int,input().split()))
print(len(nl.difference(ml)))

###034_Set .symmetric_difference() Operation
n=int(input())
nl=set(map(int,input().split()))
m=int(input())
ml=set(map(int,input().split()))
print(len(nl.symmetric_difference(ml)))

###035_Set Mutations
n=int(input())
nl=set(map(int,input().split()))
for i in range(int(input())):
    cmd=input().split()
    cl=set(map(int,input().split()))
    if cmd[0]=='intersection_update':
        nl.intersection_update(cl)
    elif cmd[0]=='update':
        nl.update(cl)
    elif cmd[0]=='symmetric_difference_update':
        nl.symmetric_difference_update(cl)
    else:
        nl.difference_update(cl)
print(sum(nl))


###036_Check Subset
for i in range(int(input())):
    n=int(input())
    nl=set(map(int,input().split()))
    m=int(input())
    ml=set(map(int,input().split()))
    if nl.intersection(ml)==nl :
        print(True)
    else:
        print(False)


for i in range(int(input())): #More than 4 lines will result in 0 score. Do not leave a blank line also. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A.issubset(B))

###037_The Captain's Room
from collections import Counter
n = int(input())
nl = list(map(int, input().split()))
chk = Counter(nl)
for key, values in chk.items():
    if values == 1:
        print(key)
        break

###
n=int(input())
nl=list(map(int,input().split()))
print(int((sum(set(nl))*n-sum(nl))/(n-1)))

###038_Check Strict Superset
chk=0
al=set(map(int,input().split()))
n=int(input())
for i in range(n):
    cl=set(map(int,input().split()))
    if len(cl)==len(cl.intersection(al)):
        chk+=1
if chk==n:
    print(True)
else:
    print(False)

###039_No Idea!
chk=0
n = input().split()
nl=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
for _ in nl :
    #print(_ in a)
    if _ in a:
        chk+=1
    #print(_ in b)
    elif _ in b:
        chk-=1  
print(chk)
'''

