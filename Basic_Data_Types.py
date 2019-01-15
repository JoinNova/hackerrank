#https://www.hackerrank.com/domains/python?badge_type=python&filters%5Bsubdomains%5D%5B%5D=py-basic-data-types
'''
###008_List Comprehensions
def Comprehensions(arg1, arg2, arg3, arg4):        
    print([[i,j,k]for i in range(arg1+1)for j in range(arg2+1)for k in range(arg3+1)if i+j+k != arg4])
if __name__ == '__main__' :
    Comprehensions(int(input()), int(input()), int(input()), int(input()))

###009_Find the Runner-Up Score!
def runner(arg1,arg2):
    print(sorted(list(set(arg2)),reverse=True)[1])
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner(n, arr)

###010_Nested Lists
if __name__ == '__main__':
    dic={}
    sl=[]
    nl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name]=score
        nl.append(name)
        sl.append(score)
    nl.sort()
    for _ in nl:
        if dic.get(_)== sorted(list(set(sl)))[1] :
            print(_)

###011_Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores    
    query_name = input()
    print('%0.2f'%(sum(student_marks[query_name])/len(student_marks[query_name])))

###012_Lists
ar = []
for _ in range(int(input())):
    cmd = input().strip()
    if cmd == 'print':
        print(ar)
    else:
        cmd = cmd.split()
        if len(cmd) == 3:
            getattr(ar, cmd[0])(int(cmd[1]), int(cmd[2]))
        elif len(cmd) == 2:
            getattr(ar, cmd[0])(int(cmd[1]))
        else:
            getattr(ar, cmd[0])()
'''
###013_Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
