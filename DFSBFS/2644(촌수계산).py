from collections import deque
import sys

def bfs(node1,node2):
    queue = deque()
    queue.append(node1)
    while queue:
        node1 = queue.popleft()
        if node1 == node2:
            return check[node2]

        for n in graph[node1]:
            if check[n] == 0:
                check[n] = check[node1]+1
                queue.append(n)
    return -1
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
s, e = map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
print(bfs(s,e))
