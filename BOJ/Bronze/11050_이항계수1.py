
#11050번 이항 계수1

a, b = 1, 1
N, K = map(int, input().split())

for i in range(N, N-K, -1) :
    a *= i

for i in range(1, K+1) :
    b *= i

print(a//b)