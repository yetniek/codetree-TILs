n, m = map(int, input().split())
jewelrys = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

jewelrys.sort(key=lambda x:-x[1]/x[0])

for w, v in jewelrys:
    if m >= w: # 현재 보석을 다 담을 수 있다면 그대로 담아줌
        m -= w
        answer += v 
    else: # 부분만 담을 수 있다면 비율에 맞춰 담아둔 뒤 종료
        answer += m / w*v
        break
print(f"{answer:.3f}")