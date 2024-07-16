n = int(input())

move = [tuple(input().split()) for _ in range(n)]

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]  

x, y = 0, 0
for m in move:
    print(m)
    d,  c = m 
    if d == 'E':
        dx, dy = dirs[0]  
        nx = x + dx * int(c)
        ny = y + dy * int(c)
    elif d == 'W':
        dx, dy = dirs[1] 
        nx = x + dx * int(c)
        ny = y + dy * int(c)
    elif d == 'S':  
        dx, dy = dirs[2]  
        nx = x + dx * int(c)
        ny = y + dy * int(c)
    elif d == 'N':
        dx, dy = dirs[3]
        nx = x + dx * int(c)
        ny = y + dy * int(c)
    x, y = nx, ny
print(x, y )