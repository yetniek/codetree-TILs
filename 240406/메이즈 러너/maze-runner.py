N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M): # 사람 : -1로 표시
    i, j = map(lambda x: int(x) - 1, input().split())
    arr[i][j] -= 1

# 비상구 -46으로 표시
ei, ej = map(lambda x: int(x) - 1, input().split())
arr[ei][ej] = -46

ans = 0 # 이동거리 합
cnt = M

def find_square(arr):
    # [1 - 비상구와 모든 사람간의 가장 짧은 가로 또는 세로 거리 구하기]
    min_dist = N
    for i in range(N):
        for j in range(N):
            if -46 < arr[i][j] < 0: # 사람인 경우
                min_dist = min(min_dist, max(abs(ei - i), abs(ej -j))) # 가로,세로 (비상구 - 각 가로 세로)

    # [2 - (0, 0) 부터 순회하면서 길이 L인 정사각형에 비상구와 사람 있는지 체크 후 리턴 (return -> L + 1)]
    for si in range(N - min_dist):
        for sj in range(N - min_dist): # 가능한 모든 시작 위치
            if si <= ei <= (si + min_dist) and sj <= ej <= (sj + min_dist):
                # 비상구가 포함된 사각형이면
                for i in range(si, si + min_dist + 1):
                    for j in range(sj, sj + min_dist + 1):
                        # 그 사각형 순회
                        if -46 < arr[i][j] < 0: # 사람이면
                            return si, sj, (min_dist + 1)

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -46:
                return i, j

for _ in range(K):
    # [1 - 모든 참가자 (동시에) 한 칸 이동(출구 최단거리 방향 상/하 우선)]
    # 출구 도착시 즉시 탈출
    new_a = [x[:] for x in arr]

    for i in range(N):
        for j in range(N):
            if -46 < arr[i][j] < 0: # 사람인 경우
                dist = abs(ei - i) + abs(ej - j) # 현재 비상구 까지의 거리
                # 네 방향 (상하 우선), 범위 내, 벽이 아니고 <= 0, 거리가 dist 보다 작으면
                # 빈칸이거나, 0, 다른 사람이 있거나, 비상구 거나
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 행렬 이동
                    ni, nj = i + di, j + dj # 상하좌우 탐색
                    if (0 <= ni < N) and (0 <= nj < N) and (arr[ni][nj] <= 0) and (dist > (abs(ei - ni) + abs(ej - nj))):
                        # 격자 범위 벗어나지 않고(유효한 범위) / 사람이고 / 현재 비상구 까지 거리 보다 작으면
                        ans += arr[i][j] # 이동 거리의 합 (현재 인원 수가 이동하는 것)
                        new_a[i][j] -= arr[i][j] # 이동 처리 다른 것과 혼동되지 않게 0이 아닌 다른 숫자로

                        if arr[ni][nj] == -46: # 비상구라면
                            cnt += arr[i][j] # 탈출
                        else: # 빈칸 또는 사람있는 자리
                            new_a[ni][nj] += arr[i][j] # 들어온 인원 추가
                        break

    arr = new_a
    if cnt == 0:
        break

    # [2 - 미로회전 (출구와 한 명 이상 참가자를 포함하는 가장 작은 정사각형)]
    # 시계방향 90도 : 같은 크기 -> 좌상단 행렬, 내구도 -1
    si, sj, L = find_square(arr) # 비상구 + 사람 포함 최소 정사각형

    new_a = [x[:] for x in arr]

    for i in range(L):
        for j in range(L):
            new_a[si + i][sj + j] = arr[si + L - 1 - j][sj + i]

            if new_a[si + i][sj + j] > 0: # 벽이면 회전시 1 감소 / 내구도가 0 이상이면 (벽이 존재 하면)
                new_a[si + i][sj + j] -= 1 # 내구도 처리

    arr = new_a
    # 회전 후 비상구 위치 저장
    ei, ej = find_exit(arr)


print(-ans)
print(ei + 1, ej + 1)