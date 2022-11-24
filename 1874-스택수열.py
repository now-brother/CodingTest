def stackIt(ans, stack):
    ans.append('+')
    stack.append(i)

def popIt(stack, ans, result, num):
    stack.append(i)
    ans.append('+')
    result.append(stack.pop())
    ans.append('-')
    num += 1

if __name__ == '__main__':
    n = int(input())

    arrInput = []
    arr = []
    for i in range(n):
        arrInput.append(int(input()))
        arr.append(i + 1)

    result = []
    stack = []
    ans = []
    num = 0
    for i in arr:
        if arrInput[num] == i:
            popIt(stack, ans, result, num)
            for j in range(len(arr), 0):
                if arrInput[num] == arr[j]:
                    popIt(stack, ans, result, num)
        else:
            stackIt(ans, stack)

    if result == arr:
        for i in ans:
            print(i)
    else:
        print('NO')