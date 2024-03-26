n = int(input())
datas = list(map(int, input().split()))

ans = 0

for i in datas: 
    if ans < 0: 
        ans = i 
    else:
        ans += i
print(ans)