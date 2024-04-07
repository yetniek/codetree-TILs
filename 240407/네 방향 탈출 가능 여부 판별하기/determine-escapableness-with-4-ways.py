from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def push(x, y):
    visited[x][y] = True
    q.append((x, y))
    
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True


def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y)

push(0, 0)
bfs()

if visited[-1][-1] == True:
    print(1)
else:
    print(0)