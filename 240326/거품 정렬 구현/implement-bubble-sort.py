n = int(input())
arr = list(map(int, input().split())

def bubble_sort():
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
bubble_sort()

for e in arr:
    print(e, end = " ")