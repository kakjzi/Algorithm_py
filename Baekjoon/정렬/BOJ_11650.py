import sys
N = int(sys.stdin.readline())
nums = [] 
for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))
nums.sort(key=lambda x: (x[0], x[1]))

for j in N: 
    print(j[0], j[1])
