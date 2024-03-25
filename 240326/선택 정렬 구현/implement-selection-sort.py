n = int(input())
arr = list(map(int, input().split()))

def select_sort():
    for i in range(n-1):
        min_ = i
        for j in range(i+1, n):
            if arr[min_] > arr[j]:
                min_ = j 
        arr[i], arr[min_] = arr[min_], arr[i]

select_sort()
for i in arr:
    print(i, end=" ")