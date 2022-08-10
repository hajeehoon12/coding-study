import sys

n = int(sys.stdin.readline())
wow =[]
for _ in range(n):
    wow.append(int(sys.stdin.readline()))

count = 0
honor = 1

wow.sort()
for i in wow:
    if i >= honor:
        count+=(i-honor)
        honor+=1

print(count)