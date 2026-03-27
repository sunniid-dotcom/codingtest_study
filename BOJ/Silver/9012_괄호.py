
#9012번 괄호

T = int(input())


for i in range(T) :
    stack = []
    ps = input()
    
    for j in ps:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
                

    else :
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

