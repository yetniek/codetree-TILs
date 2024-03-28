import heapq  
"""

힙은 특정한 규칙을 가지는 트리로
최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 함

"""

n = int(input())
nums = list(map(int, input().split()))

pq = []
answer = 0

# 작은 수를 넣는 게 항상 유리
for n in nums:
    heapq.heappush(pq, n)


while len(pq) > 1: # 원소가 2개 이상이면 
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)

    answer += (x1 + x2)
    heapq.heappush(pq, x1 + x2)

print(answer)