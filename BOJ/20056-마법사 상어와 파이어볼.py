n, m, k = map(int, input().split())

arr = []
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    arr.append([])
    arr[i].append(r)
    arr[i].append(c)
    arr[i].append(m)
    arr[i].append(s)
    arr[i].append(d)

print(arr)