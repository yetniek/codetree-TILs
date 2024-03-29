n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 람다 함수 사용해 끝나는 시간 기준으로 정렬
meetings.sort(key=lambda x: x[1])

# 가장 최근에 잡힌 회의 끝난 시간 기록하면서 meetings 리스트 돌기
last_end, answer = -1, 0
for start, end in meetings:
    if last_end <= start: # 이전 회의랑 안겹치면 해당 회의로 선택
        last_end = end
        answer += 1

print(answer)