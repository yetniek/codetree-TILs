from collections import deque


def print_board():
    global powers
    for i in range(n):
        print(powers[i])
    print('----')


def attaker_setting():
    min_p =  10000
    a_x, a_y = 0, 0  # 공격자 좌표

    for x in range(n):
        for y in range(m):
            if powers[x][y] == 0:
                continue
            # 1. 공격력 가장 낮은 포탑 선정
            if min_p > powers[x][y]:
                min_p = powers[x][y]
                a_x, a_y = x, y
            # 1-1. 공격력이 가장 낮은 포탑이 2개 이상이면
            elif min_p == powers[x][y]: 
                # 1-1-1. 가장 최근에 공격한 포탑 (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정)
                if is_attack[x][y] > is_attack[a_x][a_y]:
                    a_x, a_y = x, y  # 현재 좌표로 갱신
                # 1-2. 최근 공격한 포탑이 2개 이상이면
                elif is_attack[x][y] == is_attack[a_x][a_y]: 
                    if x + y > a_x + a_y:
                        a_x, a_y = x, y
                    # 1-3. 포탑 위치의 행과 열의 합이 같은게 2개 이상이면
                    elif x + y == a_x + a_y: 
                        # 1-3-1. 열이 가장 큰 포탑
                        if y > a_y:
                            a_y = y
    return a_x, a_y


def target_setting(attacker_x, attacker_y):
    max_p = -10000
    t_x, t_y = 0, 0  # 대상 좌표

    for x in range(n):
        for y in range(m):
            # 1. 공격력 가장 높은 포탑 선정
            if powers[x][y] == 0:  # 부서진 포탑 제외
                continue
            if x == attacker_x and y == attacker_y:  # 공격자 제외
                continue
            if max_p < powers[x][y]:
                max_p = powers[x][y]
                t_x, t_y = x, y
            # 1-1. 공격력이 가장 높은 포탑이 2개 이상이면
            elif max_p == powers[x][y]: 
                if is_attack[x][y] < is_attack[t_x][t_y]: 
                    t_x, t_y = x, y  # 현재 좌표로 갱신
                # 1-2. 최근 공격한 포탑이 2개 이상이면
                elif is_attack[x][y] == is_attack[t_x][t_y]:
                    # 1-2-1. 포탑 위치의 행과 열의 합이 가장 큰 포탑
                    if x + y < t_x + t_y:
                        t_x, t_y = x, y
                    # 1-3. 포탑 위치의 행과 열의 합이 같은게 2개 이상이면
                    elif x + y == t_x + t_y:
                        # 1-3-1. 열이 가장 큰 포탑
                        if y < t_y:
                            t_x, t_y = x, y
    return t_x, t_y


def laser(attacker_x, attacker_y, target_x, target_y): 
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((attacker_x, attacker_y, []))
    visited[attacker_x][attacker_y] = True

    while q:
        x, y, route = q.popleft()
        # 1-1. 상하좌우(우하좌상) 4개 방향 움직임
        for dx, dy in zip(dxs[:4], dys[:4]):
            # 1-3. 가장자리 범위 넘어서면 반대편으로 이동
            nx, ny = (x + dx) % n, (y + dy) % m
            if not visited[nx][ny] and powers[nx][ny] != 0:
                
                visited[nx][ny] = True  
                # 1-4. 최단 경로가 정해졌으면 공격 대상은 공격자의 공격력 만큼 피해
                if nx == target_x and ny == target_y:
                    powers[target_x][target_y] -= point
                    # 1-5. 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격자 공격력의 절반 만큼 (공격력 2로 나눈 몫)
                    for r_x, r_y in route:
                        powers[r_x][r_y] -= half_point
                        attack[r_x][r_y] = True
                    return True
                # 경로 체크
                temp_route = route[:]
                print(temp_route)
                temp_route.append((nx, ny))
                q.append((nx, ny, temp_route)) 
    return False


def shell(attack_x, attack_y, target_x, target_y):
    powers[target_x][target_y] -= point

    for dx, dy in zip(dxs, dys):
        nx, ny = (target_x + dx) % n, (target_y + dy) % m

        if nx == attack_x and ny == attack_y:
            continue
        powers[nx][ny] -= half_point
        attack[nx][ny] = True


def break_check():
    for x in range(n):
        for y in range(m):
            if powers[x][y] < 0:
                powers[x][y] = 0


def max_check():
    return max([max(p) for p in powers])


def turrent_check():
    turrent = []
    turrent_cnt = 0

    for x in range(n):
        for y in range(m):
            if powers[x][y] == 0:
                continue
            turrent_cnt += 1

            if attack[x][y]:
                continue

            turrent.append((x, y))
    if turrent_cnt == 1:
        print(max_check())
        exit(0)
    for x, y in turrent:
        powers[x][y] += 1


n, m, k = map(int, input().split())
powers = [list(map(int, input().split())) for _ in range(n)]
is_attack = [[-1] * m for _ in range(n)]
dxs, dys = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, -1, 1, -1, 1]
 
time = 0

for turn in range(k):
    attack = [[False] * m for _ in range(n)]
   # 1. 공격자 설정
    attacker_x, attacker_y = attaker_setting()
    powers[attacker_x][attacker_y] += (n + m)
  
    point = powers[attacker_x][attacker_y]
    half_point = point // 2

    attack[attacker_x][attacker_y] = True
    is_attack[attacker_x][attacker_y] = time
    time += 1

    # 2. 공격자 공격
    target_x, target_y = target_setting(attacker_x, attacker_y)
    attack[target_x][target_y] = True 
    if not laser(attacker_x, attacker_y, target_x, target_y):
        shell(attacker_x, attacker_y, target_x, target_y) 
    break_check() 
    turrent_check() 

print(max_check())