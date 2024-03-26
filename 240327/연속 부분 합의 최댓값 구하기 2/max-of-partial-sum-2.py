import sys

n = int(input())
arr = list(map(int, input().split()))

ans = -sys.maxsize
temp = 0

for i in arr:
    if temp < 0:
        temp = i
    else:
        temp += i
    ans = max(ans, temp)

    
print(ans)