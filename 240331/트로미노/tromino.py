n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]
 
def get_max_sum(x, y):
    max_sum = 0

    for i in shapes:
        sum_of_nums = 0

        for dx in range(0, 3):
            for dy in range(0, 3):
                if i[dx][dy] == 0:
                    continue
                if x+dx >= n or y+dy >= m:
                    continue
                else:
                    sum_of_nums += grid[x+dx][y+dy]
        max_sum = max(max_sum, sum_of_nums)
    return max_sum

answer = 0

for i in range(n):
    for j in range(m):
        answer = max(answer, get_max_sum(i, j))
        
print(answer)