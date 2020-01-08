import math
t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
n.sort()
for i in range(t):
    print(n[i])