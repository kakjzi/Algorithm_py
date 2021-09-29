n = int(input())

num = [1] * 10

for i in range(1,n):
    for j in range(1, 10):
        num[j] += num[j-1]

print(sum(num)%10007)