import sys
n = int(sys.stdin.readline)
num = []
for i in range(n):
    num.append(int(sys.stdin.readline))

num.sort() 
for i in range(1,n+1):
    print(i)

# sort 원본리스트 건듬
# sorted 원본리스트 말고 새로운 리스트 하나 만듬