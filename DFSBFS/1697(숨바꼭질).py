from collections import deque
import sys

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        t= q.popleft()
        print(t)
        if t ==k: # 결과에 도달시
            print(graph[t])
            break
        for nt in (t-1, t+1, t *2):
            if 0 <= nt <= (10 **5) and graph[nt]==0:
                graph[nt] = graph[t] + 1
                q.append(nt)


graph = [0] * (10 ** 5 + 1)
n, k = map(int , sys.stdin.readline().split())

bfs(n)