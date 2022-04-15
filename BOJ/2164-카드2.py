from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i)

while True:
    queue.popleft()
    queue.append[queue[0]]
    queue.popleft()
    if len(queue) == 1:
        print(queue[0])
        break