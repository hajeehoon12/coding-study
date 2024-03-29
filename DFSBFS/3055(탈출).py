import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
distance = [[0] *m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue= deque()

def bfs(Dx,Dy):
    while queue:
        x,y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"


for x in range(n): #(S처리 및 D값 저장 및 bfs함수의 인자값으로 넣기위함)
    for y in range(m):
        if graph[x][y] == 'S':
            queue.append((x,y))
        elif graph[x][y] == 'D':
            Dx,Dy = x,y

for x in range(n): #(*찾아서 넣기)
    for y in range(m):
        if graph[x][y] == '*':
            queue.append((x,y))

print(bfs(Dx,Dy))