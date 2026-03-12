
#2798 블랙잭
#브루스포트 알고리즘 (완전 탐색 알고리즘)
#시간복잡도 O(N)

maxN = -1
cnt = 0

N, M = map(int, input().split())
card = list(map(int, input().split()))

for i in range(0, N - 2) :
    for j in range(i + 1, N - 1) :
        for k in range(j + 1, N) : 
            cnt = card[i] + card[j] + card[k]
            if (cnt > maxN and cnt <= M) :
                maxN = cnt

print(maxN)