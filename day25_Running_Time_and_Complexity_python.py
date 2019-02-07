#Day 25_Running Time and Complexity_Nova
def eratos(n):
    chk=0;p='prime';N='Not prime';d=[]
    if n==1:return False
    if n%2==0:
        if n==2:return True
        else:return False
    else:
        l=list(range(3,int(n**.5)+1,2))
        for _ in l:
            if n%_==0:
                if n==_:return True
                else:return False
        return True
    
for _ in'_'*int(input()):
    print(['Not prime','Prime'][eratos(int(input()))])
