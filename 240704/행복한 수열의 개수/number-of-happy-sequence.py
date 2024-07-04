n, m = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(n)] 
seq = [0 for _ in range(n)] 

def is_happy_seq():
    consecutive_cnt, max_ccnt = 1, 1

    for i in range(1, n):
        if seq[i-1] == seq[i]:
            consecutive_cnt += 1
        else:
            consecutive_cnt = 1

        max_ccnt = max(max_ccnt, consecutive_cnt)

    return max_ccnt >= m

num_happy = 0

for i in range(n):
    seq = grid[i][:]

    if is_happy_seq():
        num_happy += 1

# vertical_lst = list(zip(*grid)) 
# for i in range(n):
#     seq = vertical_lst[i][:]

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_seq():
            num_happy += 1

print(num_happy)