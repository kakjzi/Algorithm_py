## 시간제한이 0.25초 앞서 푼 방식대로 풀면 시간제한에 걸릴듯?
## 해당 문제는 deque의 pop은 O(1)이므로 deque로 접근해보자
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().strip().split())
list = [i for i in range(1,n+1)]
answer = deque()
temp = deque() 
temp.extend(list)
num = 0
for i in range(n):
    temp.rotate(-k+1)
    answer.append(str(temp.popleft()))
print("<"+', '.join(answer)+">")



## 문자열 연결방법
# , : 띄어쓰기 포함하여 문자열을 연결한다.
# + : 띄어쓰기 미포함하여 문자열 연결한다.


## sep : 구분자를 다른 문자로 대체 가능 .


# 자꾸 시간초과가 ;;;;
