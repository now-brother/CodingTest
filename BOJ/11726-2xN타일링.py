n = int(input())

ans = [0 for i in range(n + 1)]

for i in range(1, n+1):
    if i == 1:
        ans[i] = 1
    elif i == 2:
        ans[i] = 2
    elif i == 3:
        ans[i] = 3
    else:
        ans[i] = ans[i - 1] + ans[i - 2]

print(ans[n] % 10007)