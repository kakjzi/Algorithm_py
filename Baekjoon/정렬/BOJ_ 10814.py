import sys
n = int(sys.stdin.readline())

member_list=[]
for i in range(n):
    member_list.append(sys.stdin.readline().split())

## 먼저 가입한 사람은 어차피 인덱스가 앞이니 나이만 비교해주면 됨
member_list.sort(key=lambda x: x[0])

for i in member_list:
    print(i[0], i[1])


