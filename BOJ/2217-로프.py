n = int(input())
arr = []
k = 10000

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i] < k:
        k = arr[i]

print(k*n)