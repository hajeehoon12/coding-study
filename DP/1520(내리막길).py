import sys



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y): # topdown
    if x == m-1 and y == n-1: # 끝지점일시
        return 1
    if c[x][y] != -1: #방문했을시
        return c[x][y]
    else:   # 처음일경우 연산
        c[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if a[nx][ny] < a[x][y]: # 이전값보다 작을시
                    c[x][y] += dfs(nx, ny)
        return c[x][y]

m, n = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
c = [[-1]*n for _ in range(m)] #초기화
print(dfs(0, 0))