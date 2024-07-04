n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)] 



def get_coin(i, j):
    i_s, i_e = i, i + 2
    j_s, j_e = j, j + 2
    
    coin = 0

    for i in range(i_s, i_e + 1):
        for j in range(j_s, j_e + 1):
            coin += grid[i][j]
    return coin

max_coin = 0
for i in range(n):
    for j in range(n):

        if i + 2 >= n or j + 2 >= n:
            continue
        
        coin = get_coin(i, j)
        max_coin = max(max_coin, coin)

print(max_coin)