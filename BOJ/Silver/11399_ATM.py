
#11399번 ATM

N = int(input())
P = list(map(int, input().split()))
result = 0
temp = 0

P.sort()
for i in P:
    temp += i
    result += (i + result)

print(result)