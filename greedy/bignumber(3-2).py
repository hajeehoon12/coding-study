import sys
n, m, k = map(int, sys.stdin.readline().split())

data = list(map(int , sys.stdin.readline().split()))

data.sort(reverse = True)

first = data[0]
second = data[1]

result = 0

count = int(m/(k+1))*k
count += m %(k+1)

result += count * first + (m-count)*second
    
print(result)