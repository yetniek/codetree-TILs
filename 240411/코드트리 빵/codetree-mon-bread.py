import sys
from collections import deque

N, M = map(int, input().split())
grid = [
    list(map(lambda x: int(x) - 1, input().split()))
    for _ in range(N)
]
stores = [
    tuple(map(lambda x: int(x) - 1, input().split()))
    for _ in range(M)
]

INT_MAX = sys.maxsize
EMPTY = (-1, -1) # 초기값은 격자 밖
people = [EMPTY] * M
time = 0

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
dist = [
    [0] * N
    for _ in range(N)
]
visited = [
    [False] * N
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(start_pos):
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            dist[i][j] = 0

    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = direct[i]
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 2:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

def simulate():
    for i in range(M):
        if people[i] == EMPTY or people[i] == stores[i]:
            continue

        bfs(stores[i])

        px, py = people[i]

        min_dist = INT_MAX
        min_x, min_y = -1, -1

        for i in range(4):
            dx, dy = direct[i]
            nx, ny = px + dx, py + dy
            if in_range(nx, ny) and visited[nx][ny] and min_dist > dist[nx][ny]:
                min_dist = dist[nx][ny]
                min_x, min_y = nx, ny
        people[i] = (min_x, min_y)

    for i in range(M):
        if people[i] == stores[i]:
            px, py = people[i]
            grid[px][py] = 2

    if time > M:
        return

    bfs(stores[time - 1])
    min_dist = INT_MAX
    min_x, min_y = -1, -1
    for i in range(N):
        for j in range(N):
            if visited[i][j] and grid[i][j] == 1 and min_dist > dist[i][j]:
                min_dist = dist[i][j]
                min_x, min_y = i, j

    people[time - 1] = (min_x, min_y)
    grid[min_x][min_y] = 2

def end():
    for i in range(M):
        if people[i] != stores[i]:
            return False
    return True

while True:
    time += 1
    simulate()
    if end():
        break

print(time)