
#10816번 숫자 카드 2
import sys
from collections import Counter

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a_counter = Counter(a)

for i in b :
    print(a_counter[i], end = " ")
