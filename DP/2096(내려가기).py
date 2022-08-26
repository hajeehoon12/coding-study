import sys

n= int(sys.stdin.readline())

line = []
for _ in range(n):
    line.append(list(map(int,sys.stdin.readline().split())))


max_dp = ([0] * 3) 
min_dp = ([0] * 3) 

for i in range(3):
    max_dp[i] , min_dp[i]= line[0][i],line[0][i]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            max_0 = line[i][j] + max(max_dp[j], max_dp[j + 1])
            min_0 = line[i][j] + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_1 = line[i][j] + max(max_dp)
            min_1 = line[i][j] + min(min_dp)
        elif j == 2:
            max_2 = line[i][j] + max(max_dp[j], max_dp[j - 1])
            min_2 = line[i][j] + min(min_dp[j], min_dp[j - 1])
        else:
            continue
    max_dp[0],min_dp[0] = max_0,min_0
    max_dp[1],min_dp[1] = max_1,min_1
    max_dp[2],min_dp[2] = max_2,min_2

print(max(max_dp), min(min_dp))