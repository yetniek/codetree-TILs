n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]



def get_num_of_coin(r_s, c_s, r_e, c_e):
    num_of_coin = 0
    for r in range(r_s, r_e+1):
        for c in range(c_s, c_e+1):
            num_of_coin += grid[r][c]
    return num_of_coin 

max_coin = 0
for i in range(n):
    for j in range(n):
        if i+2 >= n or j+2 >= n:
            continue
        num_of_coin = get_num_of_coin(i, j, i+2, j+2)

        max_coin = max(max_coin, num_of_coin)

print(max_coin)