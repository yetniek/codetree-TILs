def count_happy_sequences(grid, n, m):
    def is_happy_sequence(seq, m):
        count = 1
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]:
                count += 1
            else:
                count = 1
            if count >= m:
                return True
        return False
    
    happy_count = 0
    
    # Check each row
    for row in grid:
        if is_happy_sequence(row, m):
            happy_count += 1
    
    # Check each column
    for col in range(n):
        column_seq = [grid[row][col] for row in range(n)]
        if is_happy_sequence(column_seq, m):
            happy_count += 1
    
    return happy_count



n, m = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(n)] 

print(count_happy_sequences(grid, n, m))  # Output: 6

# n, m = map(int, input().split()) 
# grid = [list(map(int, input().split())) for _ in range(n)] 
# seq = [0 for _ in range(n)] 

# def is_happy_seq():
#     consecutive_cnt, max_ccnt = 1, 1

#     for i in range(1, n):
#         if seq[i-1] == seq[i]:
#             consecutive_cnt += 1
#         else:
#             consecutive_cnt = 1

#         max_ccnt = max(max_ccnt, consecutive_cnt)

#     return max_ccnt >= m

# num_happy = 0

# for i in range(n):
#     seq = grid[i][:]

#     if is_happy_seq():
#         num_happy += 1

# # vertical_lst = list(zip(*grid)) 
# # for i in range(n):
# #     seq = vertical_lst[i][:]

# for j in range(n):
#     for i in range(n):
#         seq[i] = grid[i][j]

#     if is_happy_seq():
#             num_happy += 1

# print(num_happy)