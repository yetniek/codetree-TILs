from collections import deque

n, k = map(int, input().split())
gird = [list(map(int, input().split())) for _ in range(n)]
s_x, s_y = map(lambda x: int(x) - 1, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]
ans_x, ans_y = s_x, s_y
q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, s_x, s_y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if gird[x][y] > gird[s_x][s_y]:
        return False
    return True

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num = 0
    global s_x, s_y, ans_x, ans_y

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y, s_x, s_y):

                if gird[new_x][new_y] < gird[s_x][s_y]:
                    max_num = gird[new_x][new_y]
                    ans_x, ans_y = new_x, new_y

                elif gird[new_x][new_y] == max_num:

                    if ans_x > new_x:
                        ans_x, ans_y = new_x, new_y

                    elif ans_x == new_x:
                        if ans_y > new_y:
                            ans_x, ans_y = new_x, new_y
    
    s_x, s_y = ans_x, ans_y

for _ in range(k):
    push(s_x, s_y)
    bfs()

print(s_x + 1, s_y + 1)