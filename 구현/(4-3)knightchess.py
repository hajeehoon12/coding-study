import sys
position = sys.stdin.readline()
column = int(ord(position[0]))-int(ord('a'))+1
row = int(position[1])

steps = [(-2,-1),(-1,-2),(1,-2),(1,2),(2,-1),(2,1),(-1,2),(-2,1)]

count = 0

for step in steps:
    nr = row + step[0]
    nc = column + step[1]
    if nc >=1 and nr>=1 and nc<=8 and nr<=8:
        count +=1
print(count)