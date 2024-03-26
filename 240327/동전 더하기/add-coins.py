n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0

for coin in coins[::-1]: 
    ans += k // coin # 3800 // 1000 > 3 
    k %= coin # 3800 % 1000 > 800 

print(ans)