import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)


def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    t = q.popleft()
    print(t, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[t][i] == 1:
        q.append(i)
        visit_list[i] = 1

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)