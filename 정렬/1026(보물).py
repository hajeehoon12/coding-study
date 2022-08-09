import sys

n = int(sys.stdin.readline())


A= list(map(int, sys.stdin.readline().split()))
B= list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)
result = 0
for i in range(n):
    result += A[i]*B[i]

print(result)
