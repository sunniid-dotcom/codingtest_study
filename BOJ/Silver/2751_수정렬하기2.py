
#2751 수 정렬하기2
import sys

N = int(input())
nums = []

for i in range(N) :
    nums.append(int(sys.stdin.readline()))

nums.sort()

for i in nums :
    print(i, end = " ")