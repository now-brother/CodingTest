if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline())

    dataInput = []

    for i in range(n):
        dataInput.append(sys.stdin.readline().split())

    dataInput.sort(key = lambda x : x[0])

    for i in range(n):
        print(dataInput[i][0], dataInput[i][1])