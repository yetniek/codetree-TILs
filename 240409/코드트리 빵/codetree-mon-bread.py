import sys
from collections import deque

def print_arr(arr):
    for i in arr:
        print(i, end = '\n')
    print("---------")

def in_range(r, c):
    return 0 <= r < n and 0 <= nc < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] != -100 

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
store = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

EMPTY = (-1, -1)
INI_MAX = sys.maxsize

people = [EMPTY] * n 
time = 0

drs, dcs = [-1, 0, 0, 1], [0, -1, 1, 0]
visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)] # 최단거리 결과 기록
 
# start_pos를 시작으로
# 시작점으로 부터 최단거리 결과는 step 배열에 저장
def bfs(start_pos):
    # visited, step 값 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos 
    visited[sx][sy] = True
    step[sx][sy] = 0

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if can_go(nr, nc): 
                visited[nr][nc] = True
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))

def simulation():
    # 1. 격자에 있는 사람들에 한하여 편의점 방향으로 1칸 움직임
    for i in range(m):
        # 격자 밖 or 편의점 도착
        if people[i] == EMPTY or people[i] == store[i]:
            continue
        bfs(store[i])

        pr, pc = people[i]
        min_dist = INI_MAX
        min_r, min_c = -1, -1 

        for dr, dc in zip(drs, dcs):
            nr, nc = pr + dr, pc + dc
            if in_range(nr, nc) and visited[nr][nc] and min_dist > step[nr][nc]:
                min_dist = step[nr][nc]
                min_r, min_c = nr, nc
        people[i] = (min_r, min_c)
    
    # 2. 편의점에 먼저 도착한 사람들에 한해서 앞으로 이동 불가 표시 -> grid : -100 
    for i in range(m):
        if people[i] == store[i]:
            pr, pc = people[i]
            grid[pr][pc] = -100
    
    # 3. 현재 시간 time에 대해 time <= m 을 만족하면 t가 베캠으로 이동
    # time이 m 보다 크면 패스
    if time > m:
        return
    
    # 3-1. 편점에서 가장 가까운 베캠 고르기 위해 
    # 편점을 시작으로 하는 bfs 
    bfs(store[time - 1])

    # 3-2. 편점에서 가장 가까운 베캠 선택
    min_dist = INI_MAX
    min_r, min_c = -1, -1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_r, min_c = i, j

    people[time - 1] = (min_r, min_c)
    grid[min_r][min_c] = - 100

def end():
    for i in range(m):
        if people[i] != store[i]:
            return False
    return True

while True:
    time += 1
    simulation()

    if end():
        break

print(time)