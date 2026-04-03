
#1018번 체스판 다시 칠하기

N, M = map(int, input().split())
board = []
cnt = []

for _ in range(N):
    board.append(input())

for a in range(N-7) :
    for b in range(M-7) :
        w_index = 0
        b_index = 0
        for i in range(a, a+8) : #시작지점
            for j in range(b,b+8) : #시작지점
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W' :
                        w_index += 1
                    else :
                        b_index += 1
                else:
                    if board[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        
        cnt.append(w_index)
        cnt.append(b_index)

print(min(cnt))

