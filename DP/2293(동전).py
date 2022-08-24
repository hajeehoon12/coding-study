import sys

n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for i in range(n)] # 코인초기화

dp = [0] * (k+1)

dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        if (j>=i) == 1: # 바텀업 조건
            dp[j] +=dp[j-i]
print(dp[k])