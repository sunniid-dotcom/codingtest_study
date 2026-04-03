
#11866번 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())
arr = deque(range(1, N+1))

arr2 = []

while len(arr) !=  0:
    for _ in range(K-1):
        arr.append(arr.popleft())
    arr2.append(arr.popleft())

print("<" + ", ".join(map(str, arr2)) + ">")