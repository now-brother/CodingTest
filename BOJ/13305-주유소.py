n = int(input())
arr_gasst = []
arr_range = []
for i in range(n-1):
    arr_range.append(input())
for i in range(n):
    arr_gasst.append(input())
num_min = arr_gasst[0]
for i in range(n):
    if arr_gasst[i] < num_min:
        num_min = arr_gasst[i]

for i in range(n-1):
    print(i)