import sys
n = int(sys.stdin.readline())
sort_list = [int(sys.stdin.readline()) for _ in range(n)]
[sys.stdout.write(str(value)+'\n') for value in sorted(sort_list)]

## 메모리 초과 ㅡㅡ
# 아래 코드로 변경시 O
# import sys

# N = int(sys.stdin.readline())
# nums = []
# result = [0 for _ in range(10001)]

# for i in range(N):
#     num = int(sys.stdin.readline())
#     result[num] += 1
    
# for i in range(len(result)):
#     for j in range(result[i]):
#         print(i)