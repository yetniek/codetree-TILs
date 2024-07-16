order = input()

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
initx, inity = 0, 0
num = 3
for i in order:
    if i == 'L':
        num = (num - 1 + 4) % 4
        dx, dy = dirs[num] 
    elif i == 'R':
        num = (num + 1) % 4
        dx, dy = dirs[num]
    elif i == 'F':  
        initx, inity = initx + dx, inity + dy 
 
print(initx, inity)