
#1546번 평균

N = int(input())
score_li = list(map(int, input().split()))
M = max(score_li)

for i in range(N) :
    score_li[i] = score_li[i] / M * 100

print(sum(score_li) / N)