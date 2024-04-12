from collections import deque
import sys

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

INT_MAX = sys.maxsize

attack_time = [[-1] * M for _ in range(N)]

def attacker(): 
    ax, ay = 0, 0
    minp = INT_MAX

    for i in range(N):
        for j in range(M):
            if grid[i][j] < minp:
                minp = grid[i][j]
                ax, ay = i, j
            elif gird[i][j] == minp:
                if attack_time[i][j] > attack_time[ax][ay]:
                    ax, ay = i, j
                elif attack_time[i][j] == attack_time[ax][ay]:
                    if i + j > ax + ay:
                        ax, ay = i, j
                    elif i + j == ax + ay:
                        if j > ay:
                            ax, ay = i, j
    return ax, ay

def target(ax, ay):
    tx, ty = 0, 0
    maxp = -INT_MAX

    for i in range(N):
        for j in range(M):
            if grid[i][j] > maxp:
                maxp = grid[i][j]
                tx, ty = i, j
            elif grid[i][j] == maxp:
                if attack_time[i][j] < attack_time[tx][ty]:
                    tx, ty = i, j 
                elif attack_time[i][j] == attack_time[tx][ty]:
                    if i + j < tx + ty:
                        tx, ty = i, j
                    elif i + j == tx + ty:
                        if j < ty:
                            tx, ty = i, j 
    return tx, ty

def laser(ax, ay, tx, ty):
    visited = [[False] * M for _ in range(N)]
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = deque()
    q.append((ax, ay, []))
     

    while q:
        ax, ay, route = q.popleft() 

        for d in range(4):
            dx, dy = direct[d]
            nx, ny = (ax + dx) % N, (ay + dy) % M

            if not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True

                if nx == tx and ny == ty:
                    grid[nx][ny] -= point
                    attack[nx][ny] = True
                
                for rx, ry in route:
                    grid[rx][ry] -= half_point
                    attack[rx][ry] = True

                return True
                tmp_route = route[:]
                tmp_route.append((nx, ny))
                q.append((nx, ny, tmp_route))
    return False
                
def shell(ax, ay, tx, ty):
    
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    grid[tx][ty] -= point

    for d in range(8):
        dx, dy = direct[d]
        nx, ny = (nx + dx) % N, (ny + dy) % M
        
        if nx == tx and ny == ty:
            continue
        grid[nx][ny] -= half_point
        attack[nx][ny] = True

def break_check():
    for i in range(N):
        for j in range(M):
            if grid[i][j] < 0:
                grid[i][j] = 0

def reqair():
    tower = []
    tower_cnt = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            tower_cnt += 1

            if attack[i][j]:
                continue
            tower.append((i, j))
            attak[i][j] = True

    for x, y in tower:
        grid[x][y] += 1


for turn in range(K):
    attack = [[False] * N for _ in range(N)]

    ax, ay = attacker()
    grid[ax][ay] += (M+N)
    attack[ax][ay] = True

    point = grid[ax][ay]
    half_point = point // 2

    tx, ty = target(ax, ay)
    attack[tx][ty] = True

    if not laser(ax, ay, tx, ty):
        shell(ax, ay, tx, ty)

    break_check()
    repair()

print(max([max(line) for line in grid]))