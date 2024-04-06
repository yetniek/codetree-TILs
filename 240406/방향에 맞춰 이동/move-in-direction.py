n = int(input())
directions = [list(input().split()) for _ in range(n)]

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0] 
x, y = 0, 0

dirs = {'W':0,
        'S':1,
        'N':2,
        'E':3}

for direct, cnt in directions: 
    cnt = int(cnt)
    x += dx[dirs[direct]] * cnt
    y += dy[dirs[direct]] * cnt

print(x, y)