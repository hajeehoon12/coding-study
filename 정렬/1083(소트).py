import sys

n= int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

s = int(sys.stdin.readline())

while s!=0:
    s-=1
    for i in range(n-1):
        if array[i] < array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            break
print(' '.join((str,array)))