
#11723번 집합
import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M) :
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        x = int(command[1])
        S.add(x)
    elif command[0] == 'remove':
        x = int(command[1])
        S.discard(x)
    elif command[0] == 'check':
        x = int(command[1])
        if x in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        x = int(command[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif command[0] == 'all':
        S = set(range(1, 21))
    elif command[0] == 'empty':
        S = set()