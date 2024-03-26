n = int(input())
arr = list(map(int, input().split()))
ans = 0
temp = 0
for i in arr:
    if temp < 0:
        temp = i
    else:
        temp += i
    ans = max(ans, temp)
    
    
print(ans)