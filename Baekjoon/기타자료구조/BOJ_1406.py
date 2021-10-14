# import sys
# import time
# start = time.time()
# str = list(sys.stdin.readline().strip())
# commandLine = int(sys.stdin.readline())
# strIndex = len(str)+1
# for i in range(commandLine):
#     command = input().split()
#     if command[0] == "L":
#         if strIndex > 0 : strIndex -= 1
#     elif command[0] == "D":
#         if len(str) >= strIndex : strIndex += 1
#     elif command[0] == "B":
#         if strIndex > 0: str.pop(strIndex-1)
#     elif command[0] == "P":
#         str.insert(strIndex,command[1])
# print(''.join(str))
# end = time.time()
# print(f"실행시간 : {end-start}")

# 위 코드는 시간초과 
# 최악의 경우 시간복잡도 O(N^2)임 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# for, len하고 여러가지 때문인듯??

# 접근 
# 덱을 활용하여 스택 2개를 커서를 기준으로 나눈다.
import sys
from collections import deque

string = list(input())
N = int(sys.stdin.readline())

deq = deque()
temp = deque()

deq.extend(string)

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if len(deq) != 0: temp.appendleft(deq.pop())

    elif command[0] == "D":
        if len(temp) != 0: deq.append(temp.popleft())

    elif command[0] == "B":
        if len(deq) != 0: deq.pop()

    elif command[0] == "P": deq.append(command[1])

print("".join(deq) + "".join(temp))


### deque [  , temp  ]