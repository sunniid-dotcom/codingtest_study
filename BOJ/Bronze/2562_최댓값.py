
#2562 최댓값

maxN = 0
index = 0

for i in range(9) :
    num = int(input())
    if (num > maxN) :
        maxN = num
        index = i + 1

print(maxN)
print(index)