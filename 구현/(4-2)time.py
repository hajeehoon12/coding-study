import sys
hour = int(sys.stdin.readline())

count = 0

for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)
    