import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    A,B = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((A,""))
    visit = [False] * 10000

    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        #D
        num2 = (2*num)%10000
        if not visit[num2]:
            q.append((num2,path+"D"))
            visit[num2] = True

        #S 
        num2 = (num-1)%10000
        if not visit[num2]:
            q.append((num2,path+"S"))
            visit[num2] = True
        #L
        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            q.append((num2,path+"L"))
            visit[num2] = True
            
        #R
        num2 = (num//10+(num%10)*1000)%10000
        if not visit[num2]:
            q.append((num2,path+"R"))
            visit[num2] = True