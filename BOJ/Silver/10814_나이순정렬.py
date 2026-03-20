
#10814번 나이순 정렬

N = int(input())
list = []

for i in range(N) :
    age, name = input().split()
    list.append((age, name))

list.sort(key = lambda x : int(x[0]))

for age, name in list :
    print(age, name)
