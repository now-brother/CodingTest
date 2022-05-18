n, k = map(int, input().split())

arr = list(map(int, input().split()))
arrMinus = []

for i in range(n - 1):
    arrMinus.append(arr[i + 1] - arr[i])

arrMinus.sort()

sum = 0
for i in range(n-k):
    sum += arrMinus[i]

print(sum)