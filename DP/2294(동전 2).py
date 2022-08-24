import sys

n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for i in range(n)] # 코인초기화

dp = [0] * (k+1)




for i in range(1, k+1):
    confirm = []
    for j in coin:
        if (i>=j) == 1 and dp[i-j] != -1: # 바텀업 조건
            confirm.append(dp[i-j])
    if not confirm:
        dp[i] = -1
    else:
        dp[i] = min(confirm) + 1
print(dp[k])