import sys

n = int(sys.stdin.readline())

x,y = 1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
direct_alpha = ['L','R','U','D']
direction = sys.stdin.readline().split()
nx,ny = 1,1
for i in direction:
    for j in range(4):
        if i == direct_alpha[j]:
            nx = x+dx[j]
            ny = y+dy[j]
            if (nx) <1 or (ny)<1 or (nx)>n or (ny)>n:
                continue
            x= nx
            y= ny

print(x,y)