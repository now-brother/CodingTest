arr = list(input())
countArr = []
arrAscii = []

if len(arr) == 1:
    if ord(arr[0]) > 90:
        print(chr(ord(arr[0]) - 32))
    else:
        print(arr[0])
elif len(arr) == 2:
    print('?')
else:
    for i in range(len(arr)):
        if ord(arr[i]) > 90:
            arrAscii.append(int(ord(arr[i]) - 32))
        else:
            arrAscii.append(ord(arr[i]))

    arrAscii.sort()

    cnt = 1
    for i in range(len(arrAscii) - 1):
        if arrAscii[i] == arrAscii[i + 1]:
            if i == len(arrAscii) - 2:
                cnt += 1
                countArr.append(cnt)
            else:
                cnt += 1
        else:
            countArr.append(cnt)
            cnt = 1
            if i == len(arrAscii) - 2:
                countArr.append(cnt)

    CopyArr = []
    for i in range(len(countArr)):
        CopyArr.append(countArr[i])

    CopyArr.sort(reverse = True)

    if CopyArr[0] == CopyArr[1]:
        print('?')
    else:
        max = CopyArr[0]
        for i in range(len(countArr)):
            if countArr[i] == max:
                ansIndex = 0
                for j in range(i):
                    ansIndex += countArr[j]
        print(chr(arrAscii[ansIndex]))