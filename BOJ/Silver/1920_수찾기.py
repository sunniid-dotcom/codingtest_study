
#1920번 수 찾기

def binary_search(target, data) :
    start = 0
    end = N - 1

    while start <= end :
        mid = (start + end) // 2
        if (data[mid] == target) :
            return True
        elif data[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return False

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()
for i in arr :
    if binary_search(i, A) :
        print(1)
    else :
        print(0)
    
