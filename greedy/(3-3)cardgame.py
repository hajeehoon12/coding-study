import sys
n , m = map(int , sys.stdin.readline().split())

result = 0

for i in range(n):
    data = list(map(int, sys.stdin.readline.split()))
    result =max(result, min(data))

print(result)
