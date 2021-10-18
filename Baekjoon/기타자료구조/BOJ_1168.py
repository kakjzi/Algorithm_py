## 시간제한이 0.25초 앞서 푼 방식대로 풀면 시간제한에 걸릴듯?
## 해당 문제는 deque의 pop은 O(1)이므로 deque로 접근해보자
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().strip().split())
list = [i for i in range(1,n+1)]

n,k = map(int,sys.stdin.readline().strip().split())
list = [i for i in range(1,n+1)]
answer = deque()
temp = deque() 
temp.extend(list)
num = 0


for _ in range(n):
    temp.rotate(-2)
    answer.append(str(temp.popleft()))
print("<"+', '.join(answer)+">")

for i in range(n):
    temp.rotate(-k+1)
    answer.append(str(temp.popleft()))
print("<"+', '.join(answer)+">")



## 문자열 연결방법
# , : 띄어쓰기 포함하여 문자열을 연결한다.
# + : 띄어쓰기 미포함하여 문자열 연결한다.

## sep : 구분자를 다른 문자로 대체 가능 .

## 아래는 시간초과로 인해 다른 사람 코드 참고함. 
# def delete_kth(k: int):
#         i = 1
#         while i < tree_size:
#             i += i
#             t = tree[i]
#             if t < k:
#                 k -= t
#                 i += 1
#             tree[i] -= 1
#         tree[1] -= 1
#         return i - tree_size

# N, K = [int(x) for x in input().split()]

# tree_size = 1 << (N - 1).bit_length() 
# tree = [0] * (tree_size + tree_size)
# tree[tree_size:tree_size + N] = [1] * N
# for i in range(tree_size - 1, 0, -1):
#    tree[i] = tree[i + i] + tree[i + i + 1]

# order = 0
# answer = []
# for i in range(N, 0, -1):
#    order = (order + K - 1) % i
#    num = delete_kth(order + 1)
#    answer.append(num + 1)

# print('<', end='')
# print(', '.join(str(x) for x in answer), end='>')


## sep : 구분자를 다른 문자로 대체 가능 .


# 자꾸 시간초과가 ;;;;

