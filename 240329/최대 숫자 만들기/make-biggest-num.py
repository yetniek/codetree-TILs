from functools import cmp_to_key
 
n = int(input())
nums = [int(input()) for _ in range(n)]

# custom comparator를 직접 정의
# a가 앞에 있는 숫자, b가 뒤에 있는 숫자라고 가정했을 때
# 이 순서가 우리가 원하는 순서면 -> -1
# 반대면 -> 1
# 둘의 우선순위가 동일하면 -> 0

def compare(a, b): 
    if str(a) + str(b) > str(b) + str(a):
        return -1 

    if str(a) + str(b) > str(b) + str(a):
        return 1 

    return 0


# a + b 기준 내림차순으로 정렬
nums.sort(key=cmp_to_key(compare))

for n in nums:
    print(n, end="")