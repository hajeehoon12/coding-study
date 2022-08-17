import sys

n, m = map(int, sys.stdin.readline().split())

length = list(map(int,sys.stdin.readline().split()))


start , end = 1, max(length)
while (start <= end):
    mid = (start+end)//2
    rem  = 0
    for i in length:
        if i>= mid:
            rem += i-mid
    if rem >= m:
        start = mid+1
    else:
        end = mid -1
print(end) 
