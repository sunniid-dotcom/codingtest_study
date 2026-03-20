
#1259번 펠린드롬 수

while True :
    num = input()

    if num == '0' :
        break
    if num == num[::-1] : #역순 출력 슬라이싱 이용
        print("yes")
    else :
        print("no")