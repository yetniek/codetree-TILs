n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_num_of_coin(r_s, c_s, r_e, c_e):
    num_of_coin = 0

    for r in range(r_s, r_e + 1):
        for c in range(c_s, c_e + 1): #(3,3)
            num_of_coin += grid[r][c]

    return num_of_coin

max_coin = 0

for r in range(n):
    for c in range(n):
        if c + 2 >= n or r + 2 >= n:
            continue
        
        num_of_coin = get_num_of_coin(r, c, r+2, c+2)

        max_coin = max(max_coin, num_of_coin)

print(max_coin)