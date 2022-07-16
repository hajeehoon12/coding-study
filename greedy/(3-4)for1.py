## 최소 횟수 구하는 것이 목표

import sys

from sklearn.cluster import k_means
n, m  = map(int, sys.stdin.readline().split())
count = 0

while n>= m:
    while (n%m) !=0:
        n-=1
        count += 1
    n = int(n/m)
    count+=1
count += n-1



print(count)



