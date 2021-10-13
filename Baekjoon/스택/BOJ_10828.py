import sys
N = int(sys.stdin.readline())
stack = list()

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push": stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1) if not stack else print(0)
    elif cmd[0] == "top":
        print(-1) if not stack else print(stack[-1])


# 'true일 때 명령' if true else 'true가 아닐때 명령'