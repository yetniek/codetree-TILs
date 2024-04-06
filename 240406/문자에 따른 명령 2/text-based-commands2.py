'''
시계방향 회전 -> 시계방향 기준으로 dx, dy 정의
시계방향 : 동 남 서 북
'''
directions = input()
x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

for i in directions:
    if i == 'L': # 반시계 - 방향만 이동
        dir_num = (dir_num - 1 + 4) % 4 
    elif i == 'R': # 시계 - 방향만 이동
        dir_num = (dir_num + 1) % 4 
    else: # 직진
        x += dxs[dir_num]
        y += dys[dir_num] 

print(x, y)
''' 
시계방향 90도 회전은 dx, dy를 + 1 해주면 됨(= dir_num + 1)
그런데 3일 경우 -> 0이 되어야함
따라서 ( dir_num + 1 ) % 4 
범위가 0 ~ 3 사이여야하기 때문에 나머지 연산자 사용
'''

'''
반시계방향은 -1을 해주면 됨.
다만 이 경우는 dir_num = 0 일 경우 -> 3이 되어야함
따라서 ( dir_num - 1 + 4 ) % 4 
+4 를 해주는 이유는 양수를 유지해주기 위해서임
'''