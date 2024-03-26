n = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in arr:
    if ans < 0:
        ans = i
    else:
        ans += i
print(ans)