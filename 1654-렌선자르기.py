k, n = map(int, input().split())

arr = []
sum = 0

for i in range(k):
    arr.append(int(input()))
    sum += arr[i]

num = sum // n

while True:
    sumR = 0
    for i in range(k):
        sumR += arr[i] // num

    if sumR == n:
        break
    num -= 1

print(num)