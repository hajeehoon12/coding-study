import sys
testCases = int(sys.stdin.readline())

for _ in range(testCases):
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    value = 0 
    max = 0

    for i in range(len(num)-1 , -1, -1): #거꾸로
        if(num[i] > max):
            max = num[i]
        else:
            value+= max-num[i]
    print(value)