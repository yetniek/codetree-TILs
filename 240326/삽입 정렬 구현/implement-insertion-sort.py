n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
for a in arr:
    print(a, end =" ")