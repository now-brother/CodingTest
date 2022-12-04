T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(k + 2)
    elif k == 0:
        print(n)
    