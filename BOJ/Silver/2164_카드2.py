
#2164번 카드2

from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1) :
    queue.append(i)

while len(queue) > 1 :
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
print(queue[0])