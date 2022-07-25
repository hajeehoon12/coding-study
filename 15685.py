import sys
n = int(sys.stdin.readline())

xy = [[0] * 101 for _ in range(101)] # x,y 좌표 0부터 100까지
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):

    x, y, d, g = map(int, sys.stdin.readline().split())
    xy[x][y] = 1 # 시작지점 확인
    
    # 커브 리스트 만들기
    curve = [d] # d는 방향
    
    for _ in range(g): # 세대수 만큼 반복
        for k in range(len(curve) - 1, -1, -1): # 뒤에서 부터 검사하여
            curve.append((curve[k] + 1) % 4) # 규칙을 적용해서 다음세대의 curve list에 반영
    #print(curve) # list 제대로 출력되는지 확인
    
    for j in range(len(curve)): # curve list에 들어간 방향 검사
        x += dx[curve[j]] # 방향에 해당하는 값만큼 좌표값변화
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue # 벗어나는 범위는 해당 좌표값 지정안하고 넘김

        xy[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if xy[i][j] == 1 and xy[i + 1][j] == 1 and xy[i][j + 1] == 1 and xy[i + 1][j + 1] == 1:
            result += 1

print(result)