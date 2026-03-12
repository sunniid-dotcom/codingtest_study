
#10818 최소, 최대

#최대, 최소를 구하기 위해 내장함수 쓰면 리스트를 두번 돌게 됨
# N = int(input())
# nums = list(map(int, input().split()))

# print(min(nums), max(nums))

N = int(input())
nums = map(int, input().split())

minN = 1000001
maxN = -1000001

for num in nums:
    if num < minN:
        minN = num
    if num > maxN:
        maxN = num

print(minN, maxN)
