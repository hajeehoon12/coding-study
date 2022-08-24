import sys

n = int(sys.stdin.readline())

dp = [0] * 31
dp[2] = 3

for i in range(4, n+1):
    if i %2 ==0:
        dp[i] = (dp[i-2] * dp[2]) + (sum(dp[0:i-2:2]) * 2) + 2
    else:
        continue
print(dp[n])