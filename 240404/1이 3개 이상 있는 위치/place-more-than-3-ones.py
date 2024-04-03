n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0

def is_possible(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for x in range(n):
    for y in range(n):
        cnt_of_one = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_possible(nx, ny) and grid[nx][ny] == 1:
                cnt_of_one += 1
        if cnt_of_one >= 3:
            cnt += 1
print(cnt)