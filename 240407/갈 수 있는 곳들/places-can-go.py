from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s_point = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    global ans
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y)
                ans += 1
    return ans
push(0, 0)
ans = bfs() 

print(ans)