dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(int(input())):
    p = int(input())
    for j in range(4,p+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[p])
