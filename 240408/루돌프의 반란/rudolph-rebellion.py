def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n, m, p, c, d = map(int, input().split())
grid = [[0] * n for _ in range(n)]

rudolf_x, rudolf_y = map(lambda x: int(x) - 1, input().split())
grid[rudolf_x][rudolf_y] = -1 # 루돌프 : -1

score = [0] * (p + 1) # 점수
alive = [1] * (p + 1) # 산타 살아 있는지
alive[0] = 0          # 첫 번째는 없는 산타
wakeup_turn = [1] * (p + 1) # 기절 턴 확인

santa = [[n] * 2 for _ in range(p + 1)] # [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]

for _ in range(1, p + 1):
    idx, x, y = map(int, input().split())
    santa[idx] = [x - 1, y - 1]
    grid[x - 1][y - 1] = idx

def move_santa(current, santa_x, santa_y, dx, dy, move_cnt):
    q = [(current, santa_x, santa_y, move_cnt)]

    while q:
        cur_santa, cur_x, cur_y, move_cnt = q.pop(0)
   
        nx, ny = cur_x + (dx * move_cnt), cur_y + (dy * move_cnt) # 진행방향에서 move_cnt 만큼 이동

        if 0 <= nx < n and 0 <= ny < n: # 범위 내 인지 확인
            if grid[nx][ny] == 0: # 산타 없으면
                grid[nx][ny] = cur_santa # 산타 이동
                santa[cur_santa] = [nx, ny] # 산타 자리 새로 갱신
                return
            else: # 산타 있으면 연쇄이동
                q.append((grid[nx][ny], nx, ny, 1)) # 한 칸 이동
                grid[nx][ny] = cur_santa # 이동한 산타 인덱스 저장
                santa[cur_santa] = [nx, ny] # 이동한 산타 위치 저장
        else: # 범위 내에 없으면 
            alive[cur_santa] = 0 # 죽음
            return

for turn in range(1, m + 1):
    # 산타 다 죽으면 break
    if alive.count(1) == 0:
        break

    # move_rudolf : find closer santa
    min_dist = 1000
    min_dist_list_ru = []

    for idx in range(1, p + 1):
        if alive[idx] == 0: # 산타 죽었으면 스킵
            continue

        santa_x, santa_y = santa[idx] # idx에 해당하는 산타 좌표
        dist = (rudolf_x - santa_x) ** 2 + (rudolf_y - santa_y) ** 2 # 현재 거리

        if min_dist > dist:
            min_dist = dist
            min_dist_list_ru = [(santa_x, santa_y, idx)] # 최소거리 좌표와 산타 -> 리스트에 저장

        elif min_dist == dist: # 최소거리랑 현재 거리가 같으면
            min_dist_list_ru.append((santa_x, santa_y, idx)) # 리스트에 추가

    min_dist_list_ru.sort(reverse = True) # 행이 큰 순서로 정렬
    santa_x, santa_y, min_santa_idx = min_dist_list_ru[0] # 가까운 산타 정보로 업뎃

    r_dx, r_dy = 0, 0 # 루돌프 방향 변수
    # 루돌프의 행이 산타 행 보다 크면 -1 (산타에 가까워져야하니까)
    if rudolf_x > santa_x:
        r_dx = -1
    # 루돌프의 행이 산타 행 보다 작으면 1 (산타에 가까워져야하니까)
    elif rudolf_x < santa_x:
        r_dx = 1
    # 열도 이하동문
    if rudolf_y > santa_y:
        r_dy = -1
    elif rudolf_y < santa_y:
        r_dy = 1

    grid[rudolf_x][rudolf_y] = 0 # 루돌프 현재 자리 : 0으로
    rudolf_x, rudolf_y = rudolf_x + r_dx, rudolf_y + r_dy
    grid[rudolf_x][rudolf_y] = -1 # 새로운 자리로 업데이트

    # 루돌프와 산타 충돌할 경우
    if (rudolf_x, rudolf_y) == (santa_x, santa_y):
        score[min_santa_idx] += c # 루돌프가 박았으니(코드 흐름 상 루돌프가 먼저 박음) c점 획득
        wakeup_turn[min_santa_idx] = turn + 2 # 박힌 산타. 잠 들어라. 그리고 깨어날 턴 번호 저장
        move_santa(min_santa_idx, santa_x, santa_y, r_dx, r_dy, c) # 산타 c칸 이동

    # 산타 -> 루돌프
    for idx in range(1, p + 1):
        if alive[idx] == 0: # 산타 죽었으면 스킵
            continue
        if wakeup_turn[idx] > turn: # 현재 턴에 기절 중이면 스킵
            continue

        santa_x, santa_y = santa[idx]
        min_dist = (rudolf_x - santa_x) ** 2 + (rudolf_y - santa_y) ** 2
        min_dist_list_san = []

        dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = santa_x + dx, santa_y + dy
            # nx, ny -> 아동한 산타 거리
            dist = (rudolf_x - nx) ** 2 + (rudolf_y - ny) ** 2

            if  0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= 0 and min_dist > dist: # 산타 없고, 최소거리 짧으면
                min_dist = dist
                min_dist_list_san.append((nx, ny, dx, dy))

        if len(min_dist_list_san) == 0: # 산타가 이동할 위치 없으면
            continue
        nx, ny, dx, dy = min_dist_list_san[-1] # 마지막에 추가된 가장 짧은 거리 좌표와 방향 저장

        # 루돌프 충돌 (산타 -> 루돌프)
        if (rudolf_x, rudolf_y) == (nx, ny):
            score[idx] += d # 산타가 박았으니까 + d
            wakeup_turn[idx] = turn + 2 # 잠듬
            grid[santa_x][santa_y] = 0 # 튕겨 나갔으니까 0
            move_santa(idx, nx, ny, -dx, -dy, d) # 반대로 튕기니까 - 붙음
        else:
            grid[santa_x][santa_y] = 0 # 기존 산타 위치 0으로
            grid[nx][ny] = idx # 위치 값 갱신
            santa[idx] = [nx, ny] # 위치(좌표) 갱신
            # debug
  
    for i in range(1, p + 1): # 산타 살아 있는지 체크 턴 끝날 때
        if alive[i] == 1: # 살아 있으면
            score[i] += 1 # 1점 추가

print(*score[1:])