n, m = map(int, input().split())) # 3, 2
grid = [list(map(int, input().split())) for _ in range(n)] 
# [[1, 2, 2], [1, 3, 4], [1, 2, 3]]
seq = [0 for _ in range(n)] 
# [0, 0, 0]

def is_happy_sequence(): 
    consecutive_count, max_ccnt = 1, 1

    # [1, 2, 2] in seq ver
    # [1, 1, 1] in seq hor
    for i in range(1, n): # 1~3 (1, 2)
        if seq[i - 1] == seq[i]:
            # seq[0] == seq[1] / seq[1] == seq[2]
            consecutive_count += 1
        else:
            # seq[0] != seq[1] / seq[1] != seq[2]
            consecutive_count = 1

        max_ccnt = max(max_ccnt, consecutive_count)
 
    return max_ccnt >= m # max_ccnt >= 2


num_happy = 0
 
for i in range(n):
    seq = grid[i][:]
    # [1, 2, 2] in seq ver
    # [1, 3, 4] in seq ver
    # [1, 2, 3] in seq ver
    if is_happy_sequence(): # True 면
        num_happy += 1
 
for j in range(n): # 0~3 (0, 1, 2)
    for i in range(n): # 0~3 (0, 1, 2)
        seq[i] = grid[i][j] # grid[0][0] / grid[1][1] / grid[2][2]
        '''
        1 in seq hor
        1 in seq hor
        1 in seq hor
        [1, 1, 1]
        
        2 in seq hor
        3 in seq hor
        2 in seq hor
        [2, 3, 2]
        
        2 in seq hor
        4 in seq hor
        3 in seq hor
        [2, 4, 3]
        ''' 
    if is_happy_sequence():
        num_happy += 1

print(num_happy)