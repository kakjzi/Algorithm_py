n = int(input())
dp= [0]*n
num = list(map(int, input().split()))

dp[0]=num[0]

for i in range(n):
        dp[i] = max(num[i], dp[i-1]+num[i])
print(max(dp))