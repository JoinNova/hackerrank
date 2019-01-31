#Day 18: Queues and Stacks
import sys
import collections as c
class Solution:
    # Write your code here
    def __init__(self):
        self.deq=c.deque()
        self.sta=[]
    def pushCharacter(self,string):
        self.sta+=[string]
    def enqueueCharacter(self,string):
        self.deq+=[string]
    def popCharacter(self):
        return self.sta.pop()
    def dequeueCharacter(self):
        return self.deq.popleft()
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")   
