n, t = map(int, input().split())
r, c, d = input().split()

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]
'''
0 : (0, 1) # 열 +
1 : (1, 0) # 행 -
2 : (-1, 0) # 행 +
3 : (0, -1) # 열 -
'''

mapper = {
    'R' : 0, # 열 -
    'D' : 1, # 행 -
    'U' : 2, # 행 +
    'L' : 3 # 열 +
}

move_dir = mapper[d]
r, c = int(r) - 1, int(c) - 1

def is_possible(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t): 
    nx, ny = r + dxs[move_dir], c + dys[move_dir]
    if not is_possible(nx, ny): 
        move_dir = 3 - move_dir 
    else: 
        r, c = nx, ny

print(r + 1, c + 1)