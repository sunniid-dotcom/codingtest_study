
#1181번 단어 정렬

N = int(input())
data = []

for i in range(N) :
    data.append(input())

data = list(set(data))
data.sort()
data.sort(key=len)

for i in data :
    print(i)