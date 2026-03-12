
#1978 소수찾기

cnt = 0

N = int(input())
nums = list(map(int, input().split()))

for i in nums :
    if i < 2 :
        continue

    for j in range(2, i):
        if i % j == 0:
            break

    else :
        cnt += 1
    
print(cnt)
