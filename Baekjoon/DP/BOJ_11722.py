n = int(input())

dp=[1]*1001

num =  list(map(int, input().split()))

print(num)
for i in range(1,n):
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
