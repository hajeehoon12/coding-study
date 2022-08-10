import sys

n = int(sys.stdin.readline())

c = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

c.sort(reverse= True)
b.sort(reverse= True)
time = 0
if b[0] > c[0]:
    print(-1)
    sys.exit()

else:
    while b:
        if not b:
            break
        for i in c:
            for j in b:
                if i>=j:
                    b.remove(j)
                    break
        time+=1
print(time)