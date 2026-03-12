
#30802 웰컴 키트

cnt = 0

N = int(input())
num = list(map(int, input().split()))

T, P = map(int, input().split())

for i in num :
    cnt += (i + T - 1) //T

print(cnt)
print(N // P, N % P)