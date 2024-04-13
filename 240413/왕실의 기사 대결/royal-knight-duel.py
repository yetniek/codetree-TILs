from collections import deque

moves = [(-1,0),(0,1),(1,0),(0,-1)]

# 범위 
def in_range(nx,ny,h,w):
    return 1<=nx<=L+1-h and 1<=ny<=L+1-w

# 움직임을 시도해봅니다.
def try_movement(idx, dir):
    q = deque()
    q.append(idx)
    
    # 초기화 작업입니다.
    for pid in range(1, N + 1):     # 1번 기사부터 N번 기사까지 
        dmg[pid] = 0                # 받은 데미지 0으로 초기화 
        is_moved[pid] = False       # 움직임 False로 초기화 
        nr[pid] = r[pid]            # 새로운 위치 r을 일단 현재 위치 r로 초기화
        nc[pid] = c[pid]            # 새로운 위치 c을 일단 현재 위치 c로 초기화

    is_moved[idx] = True            # 현재 기사를 기준으로 움직임 시작 
    
    while q:
        x = q.popleft()

        nr[x] += moves[dir][0]            # 새로운, 움직일 위치 
        nc[x] += moves[dir][1]

        # 경계를 벗어나는지 체크합니다.
        if not in_range(nr[x],nc[x],h[x],w[x]):
            return False        # 범위를 벗어나는 움직임이면 못 움직임

        # 함정이거나 벽인지 확인 
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if board[i][j] == 1:     # 함정이면 
                    dmg[x] += 1         # 데미지 축적 
                if board[i][j] == 2:     # 벽이 하나라도 있으면 
                    return False        # 못 움직임 

        # 대상 기사가 다른 기사와 충돌하는 경우, 해당 조각도 같이 이동합니다.
        for pid in range(1, N + 1):
            if is_moved[pid] or k[pid] <= 0:    # 이미 움직였거나, 체력이 0이하라 체스판에 없는 경우 
                continue                        # 안움직임 
            # pid 기사위치가 현재 기사의 새 위치의 범위 밖에 있으면 안옴직임 또는
            # 현재 기사의 새 위치가 pid 기사 범위 밖이면 안움직임 
            if (r[pid] > nr[x] + h[x] - 1) or (nr[x] > r[pid] + h[pid] - 1):
                continue
            if (c[pid] > nc[x] + w[x] - 1) or (nc[x] > c[pid] + w[pid] - 1):
                continue

            is_moved[pid] = True
            # 연쇄적으로 움직이게 하기 위해 큐를 사용 
            q.append(pid)       # 그 다음 움직여야 할 기사 pid         

    # return False 없이 여기까지 무사히 도달했으면 
    dmg[idx] = 0        
    return True


# 특정 조각을 지정된 방향으로 이동시키는 함수입니다.
def move_piece(idx, move_dir):
    if k[idx] <= 0:             # 체력이 0이하라 체스판에 없는 경우 
        return                  # 끝 

    # 이동이 가능한 경우,
    if try_movement(idx, move_dir): # idx 기사가 움직일 수 있는지 확인 
        for pid in range(1, N + 1): # 기사들의 실제 위치와 체력을 업데이트한다.
            r[pid] = nr[pid]
            c[pid] = nc[pid]
            k[pid] -= dmg[pid]


if __name__=="__main__":
    # L:체스판의 크기, N:기사의 수, Q:명령의 수 
    L, N, Q = map(int, input().split())
    MAX_N = 31  # 최대 기사 수 
    MAX_L = 41  # 최대 체스판 크기 
    
    board = [[2]*(L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
    
    init_k = [0 for _ in range(MAX_N)]   # 최대 개수 기사들의 초기 체력  
    r = [0]*MAX_N       # 처음 기사 위치 행 
    c = [0]*MAX_N      # 처음 기사 위치 열 
    h = [0]*MAX_N       # 기사의 범위 세로 h 
    w = [0]*MAX_N       # 기사의 범위 가로 w 
    k = [0]*MAX_N       # 기사의 체력 
    nr = [0]*MAX_N      # 기사가 움직일 위치 행 
    nc = [0]*MAX_N      # 기사가 움질일 위치 열 
    dmg = [0]*MAX_N    # 기사가 받은 데미지 
    is_moved = [False]*MAX_N    # 움직임 체크 
    
    # 기사 번호에 따른 각각의 정보를 리스트에 담는다?
    for pid in range(1, N + 1):
        r[pid], c[pid], h[pid], w[pid], k[pid] = map(int, input().split())
        init_k[pid] = k[pid]

    # Q개의 왕의 명령 
    for _ in range(Q):
        idx, d = map(int, input().split())  # i번의 기사에게 방향 d로 한칸 이동하라는 명령 
        move_piece(idx, d)

    # 결과를 계산하고 출력합니다.
    ans = sum([init_k[i] - k[i] for i in range(1, N + 1) if k[i] > 0])
    print(ans)